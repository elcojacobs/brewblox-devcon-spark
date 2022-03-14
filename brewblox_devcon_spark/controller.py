"""
Offers a functional interface to the device functionality
"""

import asyncio
import itertools
import re
from contextlib import asynccontextmanager
from typing import Callable, Union

from aiohttp import web
from brewblox_service import brewblox_logger, features, strex

from brewblox_devcon_spark import (block_cache, block_store, commander, const,
                                   exceptions, service_status, twinkeydict)
from brewblox_devcon_spark.block_analysis import is_link
from brewblox_devcon_spark.models import (Backup, BackupLoadResult, Block,
                                          BlockIdentity, BlockNameChange,
                                          FirmwareBlock, FirmwareBlockIdentity)

LOGGER = brewblox_logger(__name__)

SYNC_WAIT_TIMEOUT_S = 20
SID_PATTERN = re.compile(r'^[a-zA-Z]{1}[a-zA-Z0-9 _\-\(\)\|]{0,199}$')
SID_RULES = """
An object ID must adhere to the following rules:
- Starts with a letter
- May only contain alphanumeric characters, space, and _-()|
- At most 200 characters
"""


def merge(a: dict, b: dict):
    """Merges dict b into dict a"""
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key])
            else:
                a[key] = b[key]
        else:
            a[key] = b[key]
    return a


def resolve_data_ids(data: Union[dict, list, tuple],
                     replacer: Union[Callable[[str, str], int],
                                     Callable[[int, str], str]
                                     ]):
    iter = enumerate(data) \
        if isinstance(data, (list, tuple)) \
        else data.items()

    for k, v in iter:
        # Object-style link
        if is_link(v):
            v['id'] = replacer(v['id'], v.get('type'))
        # Postfix-style link
        elif str(k).endswith(const.OBJECT_LINK_POSTFIX_END):
            link_type = k[k.rfind(const.OBJECT_LINK_POSTFIX_START)+1:-1]
            data[k] = replacer(v, link_type)
        # Nested data - increase iteration depth
        elif isinstance(v, (dict, list, tuple)):
            resolve_data_ids(v, replacer)


class SparkController(features.ServiceFeature):

    def __init__(self, app: web.Application):
        super().__init__(app)
        self._name = app['config']['name']
        self._cmder = commander.fget(app)
        self._store = block_store.fget(app)
        self._discovery_lock: asyncio.Lock = None
        self._conn_check_lock: asyncio.Lock = None

    async def startup(self, app: web.Application):
        self._discovery_lock = asyncio.Lock()
        self._conn_check_lock = asyncio.Lock()

    def _validate_sid(self, sid: str):
        if not re.match(SID_PATTERN, sid):
            raise exceptions.InvalidId(SID_RULES)
        if next((keys for keys in const.SYS_OBJECT_KEYS if sid == keys[0]), None):
            raise exceptions.InvalidId(f'`{sid}` is an ID reserved for system objects')
        if (sid, None) in self._store:
            raise exceptions.ExistingId(f'`{sid}` is already in use')

    def _assign_sid(self, objtype: str):
        clean_name = re.sub(r',driven', '', objtype)
        for i in itertools.count(start=1):  # pragma: no cover
            name = f'{const.GENERATED_ID_PREFIX}{clean_name}-{i}'
            if (name, None) not in self._store:
                return name

    def _find_nid(self, sid: str, objtype: str) -> int:
        if sid is None:
            return 0

        if isinstance(sid, int) or sid.isdigit():
            return int(sid)

        try:
            return self._store.right_key(sid)
        except KeyError:
            raise exceptions.UnknownId(f'No numeric ID matching [sid={sid},type={objtype}] found in store')

    def _find_sid(self, nid: int, objtype: str) -> str:
        if nid is None or nid == 0:
            return None

        if isinstance(nid, str):
            raise exceptions.DecodeException(f'Expected numeric ID, got string "{nid}"')

        try:
            sid = self._store.left_key(nid)
        except KeyError:
            # If service ID not found, randomly generate one
            sid = self._assign_sid(objtype)
            self._store[sid, nid] = dict()

        return sid

    def _to_block(self, block: FirmwareBlock, find_sid=True) -> Block:
        block = Block(
            **block.dict(),
            id=None,
            serviceId=self._name
        )

        block.id = self._find_sid(block.nid, block.type) if find_sid else None
        resolve_data_ids(block.data, self._find_sid)
        return block

    def _to_firmware_block_identity(self, block: BlockIdentity) -> FirmwareBlockIdentity:
        sid = block.id
        nid = block.nid

        if nid is None:
            try:
                nid = self._store.right_key(sid)
            except KeyError:
                raise exceptions.UnknownId(f'No numeric ID matching [sid={block.id},type={block.type}] found in store')

        return FirmwareBlockIdentity(
            nid=nid,
            type=block.type,
        )

    def _to_firmware_block(self, block: Block, find_nid=True) -> FirmwareBlock:
        sid = block.id
        nid = block.nid

        if nid is None:
            try:
                nid = self._store.right_key(sid) if find_nid else 0
            except KeyError:
                raise exceptions.UnknownId(f'No numeric ID matching [sid={block.id},type={block.type}] found in store')

        block = FirmwareBlock(
            nid=nid,
            type=block.type,
            data=block.data
        )
        resolve_data_ids(block.data, self._find_nid)
        return block

    async def _check_connection(self):
        """
        Sends a Noop command to controller to evaluate the connection.
        If this command also fails, prompt the commander to reconnect.

        Only do this when the service is synchronized,
        to avoid weird interactions when prompting for a handshake.
        """
        async with self._conn_check_lock:
            if await service_status.wait_synchronized(self.app, wait=False):
                LOGGER.info('Checking connection...')
                try:
                    await self._cmder.noop()
                except Exception:
                    await self._cmder.start_reconnect()

    @asynccontextmanager
    async def _execute(self, desc: str):
        """
        Generic wrapper for all controller commands.
        State-related preconditions are checked, and errors are handled.

        Args:
            desc (str):
                Human-readable function description, to be used in error messages.
        """
        if await service_status.wait_updating(self.app, wait=False):
            raise exceptions.UpdateInProgress('Update is in progress')

        await asyncio.wait_for(
            service_status.wait_synchronized(self.app),
            SYNC_WAIT_TIMEOUT_S)

        try:
            yield

        except exceptions.CommandTimeout as ex:
            # Wrap in a task to not delay the original response
            asyncio.create_task(self._check_connection())
            raise ex

        except Exception as ex:
            LOGGER.debug(f'Failed to execute {desc}: {strex(ex)}')
            raise ex

    async def noop(self) -> None:
        """
        Send a Noop command to the controller.
        No data is written, but a welcome message is triggered as side effect.
        """
        async with self._execute('Noop'):
            await self._cmder.noop()

    async def read_block(self, block: BlockIdentity) -> Block:
        """
        Read block on controller.

        Args:
            block (BlockIdentity):
                An object containing at least a block sid or nid.
                It is valid for `block` to be a complete block,
                but all fields except the id and type will be ignored.

        Returns:
            Block:
                The desired block, as present on the controller.
        """
        async with self._execute('Read block'):
            block = self._to_firmware_block_identity(block)
            block = await self._cmder.read_object(block)
            block = self._to_block(block)
            block_cache.set(self.app, block)
            return block

    async def read_logged_block(self, block: BlockIdentity) -> Block:
        """
        Read block on controller.
        Block data is formatted to be suitable for logging.

        Args:
            block (BlockIdentity):
                An object containing at least a block sid or nid.
                It is valid for `block` to be a complete block,
                but all fields except the id and type will be ignored.

        Returns:
            Block:
                The desired block, as present on the controller.
                Block data will only include fields explicitly
                marked for logging, and units will use the postfixed format.
        """
        async with self._execute('Read block (logged)'):
            block = self._to_firmware_block_identity(block)
            block = await self._cmder.read_logged_object(block)
            block = self._to_block(block)
            return block

    async def read_stored_block(self, block: BlockIdentity) -> Block:
        """
        Read block on controller.
        Block data will only include persistent fields.

        Args:
            block (BlockIdentity):
                An object containing at least a block sid or nid.
                It is valid for `block` to be a complete block,
                but all fields except the id and type will be ignored.

        Returns:
            Block:
                The desired block, as present on the controller.
                Block data will only include fields that are stored
                in persistent memory on the controller.
                Non-persistent fields will be absent or set to a default value.
        """
        async with self._execute('Read block (stored)'):
            block = self._to_firmware_block_identity(block)
            block = await self._cmder.read_stored_object(block)
            block = self._to_block(block)
            return block

    async def write_block(self, block: Block) -> Block:
        """
        Write to a pre-existing block on the controller.

        Args:
            block (Block):
                A complete block. Either sid or nid may be omitted,
                but all data should be present. No attempt is made
                to merge new and existing data.

        Returns:
            Block:
                The desired block, as present on the controller after writing.
        """
        async with self._execute('Write block'):
            block = self._to_firmware_block(block)
            block = await self._cmder.write_object(block)
            block = self._to_block(block)
            block_cache.set(self.app, block)
            return block

    async def patch_block(self, partial: Block) -> Block:
        """
        Write to a pre-existing block on the controller.
        Data in `partial` is locally merged with last-known block data before writing.
        Existing block data is read from the controller if the block is not
        present in the service-side cache.

        Args:
            block (Block):
                A complete block. Either sid or nid may be omitted,
                and existing data will be used for all fields not set in block data.

        Returns:
            Block:
                The desired block, as present on the controller after writing.
        """
        async with self._execute('Patch block'):
            block = block_cache.get(self.app, partial) or await self.read_block(partial)
            block = block.copy(deep=True)
            merge(block.data, partial.data)
            return await self.write_block(block)

    async def create_block(self, block: Block) -> Block:
        """
        Create a new block on the controller.
        sid must be set, but nid will be auto-assigned by the controller
        if not set or 0.
        The block will not be created if either sid or nid is already in use.

        Args:
            block (Block):
                A complete block.

        Returns:
            Block:
                The desired block, as present on the controller after creation.
        """

        async with self._execute('Create block'):
            desired_sid = block.id
            self._validate_sid(desired_sid)
            block = self._to_firmware_block(block, find_nid=False)

            # Avoid race conditions for the desired sid
            # Claim it with a placeholder until the spark create call returns
            placeholder_nid = object()
            self._store[desired_sid, placeholder_nid] = 'PLACEHOLDER'

            try:
                block = await self._cmder.create_object(block)
            finally:
                del self._store[desired_sid, placeholder_nid]

            # The placeholder is always removed - add real entry if create was ok
            self._store[desired_sid, block.nid] = dict()

            block = self._to_block(block)
            block_cache.set(self.app, block)
            return block

    async def delete_block(self, block: BlockIdentity) -> BlockIdentity:
        """
        Remove block on the controller.
        Will raise an error if the block is not present.

        Args:
            block (BlockIdentity):
                An object containing at least a block sid or nid.
                It is valid for `block` to be a complete block,
                but all fields except the id and type will be ignored.

        Returns:
            BlockIdentity:
                The actual sid, nid, and type of the removed block.
        """
        async with self._execute('Delete block'):
            block = self._to_firmware_block_identity(block)
            await self._cmder.delete_object(block)

            nid = block.nid
            sid = self._store.left_key(nid)
            del self._store[sid, nid]
            ident = BlockIdentity(
                id=sid,
                nid=nid,
                type=block.type,
                serviceId=self._name,
            )
            block_cache.delete(self.app, ident)
            return ident

    async def list_blocks(self) -> list[Block]:
        """
        Read all blocks on the controller.
        No particular order is guaranteed.

        Returns:
            list[Block]:
                All present blocks on the controller.
        """
        async with self._execute('Read all blocks'):
            blocks = await self._cmder.list_objects()
            blocks = [self._to_block(v) for v in blocks]
            block_cache.set_all(self.app, blocks)
            return blocks

    async def list_logged_blocks(self) -> list[Block]:
        """
        Read all blocks on the controller.
        Block data is formatted to be suitable for logging.

        Returns:
            list[Block]:
                All present blocks on the controller.
                Block data will only include fields explicitly
                marked for logging, and units will use the postfixed format.
        """
        async with self._execute('Read all blocks (logged)'):
            blocks = await self._cmder.list_logged_objects()
            blocks = [self._to_block(v) for v in blocks]
            return blocks

    async def list_stored_blocks(self) -> list[Block]:
        """
        Read all blocks on the controller.
        Block data is formatted to be suitable for logging.

        Returns:
            list[Block]:
                All present blocks on the controller.
                Block data will only include fields that are stored
                in persistent memory on the controller.
                Non-persistent fields will be absent or set to a default value.
        """
        async with self._execute('Read all blocks (stored)'):
            blocks = await self._cmder.list_stored_objects()
            blocks = [self._to_block(v) for v in blocks]
            return blocks

    async def list_broadcast_blocks(self) -> tuple[list[Block], list[Block]]:
        """
        Read all blocks on the controller.
        The same raw data is formatted both normally, and suitable for logging.

        Returns:
            tuple[list[Block], list[Block]]:
                All present blocks on the controller.
                The first list in the tuple will be formatted normally,
                the second is suitable for logging.
        """
        async with self._execute('Read all blocks (broadcast)'):
            blocks, logged_blocks = await self._cmder.list_broadcast_objects()
            blocks = [self._to_block(v) for v in blocks]
            logged_blocks = [self._to_block(v) for v in logged_blocks]
            block_cache.set_all(self.app, blocks)
            return (blocks, logged_blocks)

    async def discover_blocks(self) -> list[Block]:
        """
        Discover blocks for newly connected OneWire devices.
        The controller will create new blocks during discovery,
        and the new block will only be yielded during a single discovery.

        Returns:
            list[Block]:
                Newly discovered blocks.
        """
        async with self._execute('Discover blocks'):
            async with self._discovery_lock:
                blocks = await self._cmder.discover_objects()
            blocks = [self._to_block(v) for v in blocks]
            return blocks

    async def clear_blocks(self) -> list[BlockIdentity]:
        """
        Remove all user-created blocks on the controller.
        System blocks will not be removed, but the display settings
        will be reset.

        Returns:
            list[BlockIdentity]:
                The ids of all removed blocks.
        """
        async with self._execute('Remove all blocks'):
            await self._cmder.clear_objects()
            self._store.clear()
            await self._cmder.write_object(FirmwareBlock(
                nid=const.DISPLAY_SETTINGS_NID,
                type='DisplaySettings',
                data={},
            ))
            ids = [BlockIdentity(id=sid, nid=nid, serviceId=self._name)
                   for (sid, nid) in block_cache.keys(self.app)
                   if nid >= const.USER_NID_START]
            block_cache.delete_all(self.app)
            return ids

    async def rename_block(self, change: BlockNameChange) -> BlockIdentity:
        """
        Change a block sid.
        This will not change any data on the controller,
        as block string IDs are stored in the datastore.

        Args:
            change (BlockNameChange):
                Existing and desired ID for the block.

        Returns:
            BlockIdentity:
                The new sid + nid.
        """
        self._validate_sid(change.desired)
        self._store.rename((change.existing, None), (change.desired, None))
        block_cache.rename(self.app, change.existing, change.desired)
        return BlockIdentity(
            id=change.desired,
            nid=self._store.right_key(change.desired),
            serviceId=self._name
        )

    async def remove_unused_ids(self) -> list[BlockIdentity]:
        """
        Compares blocks on the controller with block sid/nid entries
        in the datastore, and removes unused entries.

        Returns:
            list[BlockIdentity]:
                Unused (and now removed) block IDs.
        """
        actual = [block.id
                  for block in await self.list_blocks()]
        unused = [(sid, nid)
                  for (sid, nid) in self._store
                  if sid not in actual]
        for (sid, nid) in unused.copy():
            del self._store[sid, nid]
        return [BlockIdentity(id=sid, nid=nid, serviceId=self._name)
                for (sid, nid) in unused]

    async def backup_save(self) -> Backup:
        """
        Exports blocks and block datastore entries to a serializable format
        This only includes persistent data fields for all blocks.

        Returns:
            Backup:
                JSON-ready backup data, compatible with backup_load().
        """
        store_data = [{'keys': keys, 'data': content}
                      for keys, content in self._store.items()]
        blocks_data = await self.list_stored_blocks()
        return Backup(
            blocks=[block for block in blocks_data
                    if block.nid != const.SYSTIME_NID],
            store=store_data,
        )

    async def backup_load(self, exported: Backup) -> BackupLoadResult:
        """
        Loads backup data generated by backup_save().
        Blocks are not merged with the current controller state:
        all existing created blocks are removed before the backup is loaded.

        The loader attempts to continue on error.
        If any block could not be created, the error will be logged and suppressed.

        Args:
            exported (Backup):
                Data as exported earlier by backup_save().

        Returns:
            BackupLoadResult:
                User feedback on errors encountered during import.
        """
        async with self._discovery_lock:
            await self.clear_blocks()
            error_log = []

            # First populate the datastore, to avoid unknown links
            for entry in exported.store:
                keys = entry['keys']
                data = entry['data']

                try:
                    self._store[keys] = data
                except twinkeydict.TwinKeyError:
                    sid, nid = keys
                    self._store.rename((None, nid), (sid, None))
                    self._store[keys] = data

            # Now either create or write the objects, depending on whether they are system objects
            for block in exported.blocks:
                try:
                    if block.nid in const.DEPRECATED_NIDS:
                        continue

                    block = block.copy(deep=True)
                    if block.nid is not None and block.nid < const.USER_NID_START:
                        await self.write_block(block)
                    else:
                        # Bypass self.create_block(), to avoid meddling with store IDs
                        await self._cmder.create_object(
                            self._to_firmware_block(block))

                except Exception as ex:
                    message = f'failed to import block. Error={strex(ex)}, block={block}'
                    error_log.append(message)
                    LOGGER.error(message)

            used_nids = [b.nid for b in await self.list_blocks()]
            unused = [
                (sid, nid) for (sid, nid) in self._store
                if nid >= const.USER_NID_START
                and nid not in used_nids
            ]
            for sid, nid in unused:
                del self._store[sid, nid]
                message = f'Removed unused alias [{sid},{nid}]'
                LOGGER.info(message)
                error_log.append(message)

            return BackupLoadResult(messages=error_log)

    async def factory_reset(self) -> None:
        """
        Prompt the controller to perform a factory reset.
        This function will return immediately after writing the command.
        """
        async with self._execute('Factory reset'):
            await self._cmder.factory_reset()

    async def reboot(self) -> None:
        """
        Prompt the controller to reboot itself.
        This function will return immediately after writing the command.
        """
        async with self._execute('Reboot'):
            await self._cmder.reboot()

    async def validate(self, block: Block) -> Block:
        """
        Encode and validate the provided block.
        The block will not be written to the controller,
        and does not have to be an existing block.

        Args:
            block (Block):
                A block that at least includes type and data.
                Both sid and nid may be omitted.
        """
        async with self._execute('Validate block'):
            block = self._to_firmware_block(block, find_nid=False)
            block = await self._cmder.validate(block)
            block = self._to_block(block, find_sid=False)
            return block


def setup(app: web.Application):
    features.add(app, SparkController(app))


def fget(app: web.Application) -> SparkController:
    return features.get(app, SparkController)

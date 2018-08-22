"""
Regulates actions that should be taken when the service connects to a controller.
"""


import asyncio
import json

import aiofiles
from aiohttp import web
from brewblox_service import brewblox_logger, features, scheduler

from brewblox_devcon_spark import exceptions, status
from brewblox_devcon_spark.api import (API_DATA_KEY, API_ID_KEY,
                                       API_PROFILE_LIST_KEY, API_TYPE_KEY,
                                       object_api, system_api)

LOGGER = brewblox_logger(__name__)


def setup(app: web.Application):
    features.add(app, Seeder(app))


def get_seeder(app: web.Application):
    return features.get(app, Seeder)


class Seeder(features.ServiceFeature):

    def __init__(self, app: web.Application):
        super().__init__(app)

        self._config = app['config']
        self._task: asyncio.Task = None

    async def startup(self, app: web.Application):
        await self.shutdown(app)
        self._task = await scheduler.create_task(app, self._seed())

    async def shutdown(self, _):
        await scheduler.cancel_task(self.app, self._task)
        self._task = None

    async def _seed(self):
        spark_status = status.get_status(self.app)

        while True:
            await spark_status.connected.wait()
            await self._seed_objects()
            await self._seed_profiles()
            await spark_status.disconnected.wait()

    ##########

    async def _seed_objects(self):
        seed_file = self._config['seed_objects']
        if not seed_file:
            return

        try:
            async with aiofiles.open(seed_file) as f:
                seeds = json.loads(await f.read())
        except Exception as ex:
            LOGGER.warn(f'Failed to read seed file {seed_file} {type(ex).__name__}({ex})')
            return

        api = object_api.ObjectApi(self.app)
        for seed in seeds:
            try:
                id = seed[API_ID_KEY]
                await api.create(
                    id,
                    seed[API_PROFILE_LIST_KEY],
                    seed[API_TYPE_KEY],
                    seed[API_DATA_KEY]
                )
                LOGGER.info(f'Seeded [{id}]')

            except exceptions.ExistingId:
                LOGGER.warn(f'Skipped seeding [{id}]: duplicate name, or already created')

            except Exception as ex:
                LOGGER.warn(f'Failed to seed object: {type(ex).__name__}({ex})')

    async def _seed_profiles(self):
        if not self._config['seed_profiles']:
            return

        try:
            api = system_api.SystemApi(self.app)
            profiles = self._config['seed_profiles']
            await api.write_profiles(profiles)

        except Exception as ex:
            LOGGER.warn(f'Failed to seed profiles {profiles} {type(ex).__name__}({ex})')

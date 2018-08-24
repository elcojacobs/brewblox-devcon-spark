"""
Tests brewblox_devcon_spark.commander_sim
"""

import pytest

from brewblox_devcon_spark import (commander, commander_sim, commands,
                                   exceptions, status)
from brewblox_devcon_spark.codec import codec
from brewblox_devcon_spark.commands import (OBJECT_DATA_KEY, OBJECT_ID_KEY,
                                            OBJECT_LIST_KEY, OBJECT_TYPE_KEY,
                                            PROFILE_LIST_KEY)


@pytest.fixture
def app(app):
    status.setup(app)
    commander_sim.setup(app)
    codec.setup(app)
    return app


@pytest.fixture
def sim(app):
    return commander.get_commander(app)


@pytest.fixture
def object_args():
    return {
        PROFILE_LIST_KEY: [0],
        OBJECT_TYPE_KEY: 257,  # OneWireTempSensor
        OBJECT_DATA_KEY: b'\x00'
    }


async def test_create(app, client, object_args, sim):
    cmd = commands.CreateObjectCommand

    created = await sim.execute(cmd.from_args(**object_args))
    assert 'object_id' in created

    # Ok to recreate without ID
    other = await sim.execute(cmd.from_args(**object_args))
    assert other != created

    # Object ID already exists
    with pytest.raises(exceptions.CommandException):
        await sim.execute(cmd.from_args(**created))


async def test_crud(app, client, object_args, sim):
    create_cmd = commands.CreateObjectCommand
    delete_cmd = commands.DeleteObjectCommand
    read_cmd = commands.ReadObjectCommand
    write_cmd = commands.WriteObjectCommand

    created = await sim.execute(create_cmd.from_args(**object_args))

    read_args = {
        OBJECT_ID_KEY: created[OBJECT_ID_KEY],
        OBJECT_TYPE_KEY: created[OBJECT_TYPE_KEY]
    }
    assert await sim.execute(read_cmd.from_args(**read_args)) == created

    created[PROFILE_LIST_KEY] = [0, 1, 7]
    assert await sim.execute(write_cmd.from_args(**created)) == created
    assert await sim.execute(read_cmd.from_args(**read_args)) == created

    await sim.execute(delete_cmd.from_args(object_id=read_args[OBJECT_ID_KEY]))

    with pytest.raises(exceptions.CommandException):
        assert await sim.execute(write_cmd.from_args(**created))

    with pytest.raises(exceptions.CommandException):
        assert await sim.execute(read_cmd.from_args(**read_args))


async def test_clear(app, client, object_args, sim):
    create_cmd = commands.CreateObjectCommand
    list_cmd = commands.ListActiveObjectsCommand
    clear_cmd = commands.ClearObjectsCommand

    await sim.execute(create_cmd.from_args(**object_args))
    pre = await sim.execute(list_cmd.from_args())
    await sim.execute(clear_cmd.from_args())
    post = await sim.execute(list_cmd.from_args())

    assert len(post[OBJECT_LIST_KEY]) == len(pre[OBJECT_LIST_KEY]) - 1


async def test_noops(app, client, sim):
    for cmd in [
        commands.FactoryResetCommand,
        commands.RebootCommand
    ]:
        assert await sim.execute(cmd.from_args()) == {}
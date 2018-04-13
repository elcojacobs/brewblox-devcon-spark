"""
Tests brewblox_devcon_spark.api
"""

import pytest
from asynctest import CoroutineMock
from brewblox_devcon_spark import api, commander, datastore, device

TESTED = api.__name__


@pytest.fixture
def object_args():
    return dict(
        id='testobj',
        type=6,
        data=dict(
            settings=dict(
                address='FF',
                offset=20
            ),
            state=dict(
                value=12345,
                connected=True
            )
        )
    )


@pytest.fixture
def commander_mock(mocker, loop):
    cmder = commander.SparkCommander(loop=loop)

    def echo(command):
        retval = command.decoded_request
        retval['command'] = command.name
        return retval

    cmder.write = CoroutineMock()
    cmder.do = CoroutineMock()
    cmder.execute = CoroutineMock()
    cmder.execute.side_effect = echo
    return cmder


@pytest.fixture
def object_store():
    return datastore.MemoryDataStore(primary_key=device.SERVICE_ID_KEY)


@pytest.fixture
def system_store():
    return datastore.MemoryDataStore(primary_key=device.SERVICE_ID_KEY)


@pytest.fixture
def object_cache():
    return datastore.MemoryDataStore(primary_key=device.SERVICE_ID_KEY)


@pytest.fixture
def controller_mock(mocker, commander_mock, object_store, system_store, object_cache):
    controller = device.SparkController('sparky')
    controller._commander = commander_mock
    controller._object_store = object_store
    controller._system_store = system_store
    controller._object_cache = object_cache

    mocker.patch(device.__name__ + '.get_controller').return_value = controller
    return controller


@pytest.fixture
async def app(app, controller_mock, object_store, system_store, loop):
    """App + controller routes"""
    api.setup(app)

    await object_store.start(loop=loop)
    await object_store.create_by_id('testobj', dict(controller_id=[1, 2, 3]))

    await system_store.start(loop=loop)
    await system_store.create_by_id('sysobj', dict(controller_id=[3, 2, 1]))

    return app


async def test_write(app, client, commander_mock):
    commander_mock.write.return_value = 'reply'

    res = await client.post('/_debug/write', json=dict(command='text'))
    assert res.status == 200
    assert (await res.json()) == dict(written='reply')
    assert commander_mock.write.call_count == 1


async def test_do(app, client, commander_mock):
    command = dict(command='abracadabra', kwargs=dict(magic=True))
    retval = dict(response='ok')
    commander_mock.do.return_value = retval

    res = await client.post('/_debug/do', json=command)
    assert res.status == 200
    assert (await res.json()) == retval
    assert commander_mock.do.call_count == 1


async def test_create(app, client, object_args):
    res = await client.post('/objects', json=object_args)
    assert res.status == 500  # testobj already exists

    object_args['id'] = 'other_obj'
    res = await client.post('/objects', json=object_args)
    assert res.status == 200
    assert (await res.json())['type'] == object_args['type']


async def test_read(app, client):
    res = await client.get('/objects/testobj')
    assert res.status == 200

    retval = await res.json()
    assert retval['command'] == 'READ_VALUE'
    assert retval['id'] == [1, 2, 3]


async def test_update(app, client, object_args):
    res = await client.put('/objects/testobj', json=object_args)
    assert res.status == 200
    retval = await res.json()
    assert retval['command'] == 'WRITE_VALUE'


async def test_delete(app, client):

    res = await client.delete('/objects/testobj')
    assert res.status == 200
    retval = await res.json()
    assert retval['command'] == 'DELETE_OBJECT'
    assert retval['id'] == [1, 2, 3]


async def test_all(app, client):
    res = await client.get('/objects')
    assert res.status == 200
    retval = await res.json()
    assert retval['command'] == 'LIST_OBJECTS'


async def test_system_read(app, client):
    res = await client.get('/system/sysobj')
    assert res.status == 200

    retval = await res.json()
    assert retval['command'] == 'READ_SYSTEM_VALUE'
    assert retval['id'] == [3, 2, 1]


async def test_system_update(app, client, object_args):
    res = await client.put('/system/sysobj', json=object_args)
    assert res.status == 200
    retval = await res.json()
    assert retval['command'] == 'WRITE_SYSTEM_VALUE'


async def test_profile_create(app, client):
    res = await client.post('/profiles')
    assert res.status == 200

    retval = await res.json()
    assert retval['command'] == 'CREATE_PROFILE'


async def test_profile_delete(app, client):
    res = await client.delete('/profiles/1')
    assert res.status == 200

    retval = await res.json()
    assert retval['command'] == 'DELETE_PROFILE'


async def test_profile_activate(app, client):
    res = await client.post('/profiles/1')
    assert res.status == 200

    retval = await res.json()
    assert retval['command'] == 'ACTIVATE_PROFILE'


async def test_command_exception(app, client, commander_mock):
    commander_mock.execute.side_effect = RuntimeError('test error')

    res = await client.post('/profiles')
    assert res.status == 500

    retval = await res.json()
    assert 'test error' in retval['error']


async def test_alias_create(app, client):
    new_alias = dict(
        alias='name',
        controller_id=[4, 5, 6]
    )
    res = await client.post('/aliases', json=new_alias)
    assert res.status == 200

    res = await client.post('/aliases', json=new_alias)
    assert res.status == 500


async def test_alias_update(app, client):
    res = await client.get('/objects/newname')
    assert res.status == 500

    res = await client.put('/aliases/testobj', json=dict(alias='newname'))
    assert res.status == 200

    res = await client.get('/objects/newname')
    assert res.status == 200

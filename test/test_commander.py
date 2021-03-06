"""
Tests brewblox_devcon_spark.commander
"""

import asyncio
from datetime import timedelta

import pytest
from brewblox_service import scheduler
from mock import AsyncMock, PropertyMock

from brewblox_devcon_spark import (commander, commands, const, exceptions,
                                   service_status)

TESTED = commander.__name__


@pytest.fixture
def reset_msgid():
    commands.Command._msgid = 0


@pytest.fixture
def conduit_mock(mocker):
    m = mocker.patch(TESTED + '.communication.get_conduit')
    m.return_value.bind = AsyncMock()
    m.return_value.write = AsyncMock()
    m.return_value.shutdown = AsyncMock()
    m.return_value.disconnect = AsyncMock()
    return m.return_value


@pytest.fixture
def app(app, conduit_mock, mocker):
    app['config']['command_timeout'] = 1
    service_status.setup(app)
    scheduler.setup(app)
    commander.setup(app)
    return app


@pytest.fixture
async def sparky(app, client):
    return commander.get_commander(app)


@pytest.fixture
async def welcome():
    return [
        'BREWBLOX',
        'ed70d66f0',
        '3f2243a',
        '2019-06-18',
        '2019-06-18',
        '1.2.1-rc.2',
        'p1',
        '78',
        '0A',
        '1234567F0CASE'
    ]


@pytest.fixture
async def cbox_err():
    return [
        'CBOXERROR',
        '0C',
    ]


async def test_init(conduit_mock, app, client):
    spock = commander.SparkCommander(app)

    await spock.shutdown(app)
    await spock.startup(app)
    await spock.shutdown(app)
    await spock.shutdown(app)

    assert str(spock)


async def test_on_data(conduit_mock, sparky):
    assert len(sparky._requests) == 0

    await sparky._on_data(conduit_mock, '05 00 |00 00 00 00')
    await asyncio.sleep(0.0001)
    assert len(sparky._requests) == 1
    assert sparky._requests['0500'].queue.qsize() == 1


async def test_on_data_error(mocker, conduit_mock, sparky):
    logger_mock = mocker.spy(commander, 'LOGGER')

    # No response pipe
    await sparky._on_data(conduit_mock, '1234')
    assert len(sparky._requests) == 0
    assert logger_mock.error.call_count == 1

    # Valid hex, not an opcode
    # process_response does not validate - it will be cleaned up later
    await sparky._on_data(conduit_mock, 'BB|AA')
    assert len(sparky._requests) == 1
    assert logger_mock.error.call_count == 1


async def test_on_event(mocker, conduit_mock, sparky):
    logger_mock = mocker.spy(commander, 'LOGGER')
    await sparky._on_event(conduit_mock, 'hello')
    assert logger_mock.info.call_count == 1


async def test_on_welcome(app, mocker, conduit_mock, sparky, welcome):
    status = service_status.get_status(app)
    service_status.set_connected(app, 'addr')
    assert service_status.desc(app).device_address == 'addr'

    ok_msg = ','.join(welcome)
    nok_welcome = welcome.copy()
    nok_welcome[2] = 'NOPE'
    nok_msg = ','.join(nok_welcome)
    await sparky._on_event(conduit_mock, ok_msg)
    assert service_status.desc(app).handshake_info.is_compatible_firmware

    status.service_info.device_id = '1234567f0case'
    await sparky._on_event(conduit_mock, ok_msg)
    assert service_status.desc(app).handshake_info.is_valid_device_id

    status.service_info.device_id = '01345'
    with pytest.warns(UserWarning, match='Handshake error'):
        await sparky._on_event(conduit_mock, ok_msg)
    assert not service_status.desc(app).handshake_info.is_valid_device_id

    status.service_info.device_id = None
    app['config']['skip_version_check'] = True
    await sparky._on_event(conduit_mock, nok_msg)
    assert service_status.desc(app).handshake_info.is_compatible_firmware

    app['config']['skip_version_check'] = False
    with pytest.warns(UserWarning, match='Handshake error'):
        await sparky._on_event(conduit_mock, nok_msg)
    assert not service_status.desc(app).handshake_info.is_compatible_firmware
    assert not service_status.desc(app).is_synchronized


async def test_on_cbox_err(app, mocker, conduit_mock, sparky, cbox_err):
    service_status.set_connected(app, 'addr')
    assert service_status.desc(app).device_address == 'addr'

    msg = ':'.join(cbox_err)
    await sparky._on_event(conduit_mock, msg)

    # shouldn't fail on non-existent error message
    msg = ':'.join([cbox_err[0], 'ffff'])
    await sparky._on_event(conduit_mock, msg)

    # shouldn't fail on invalid error
    msg = ':'.join([cbox_err[0], 'not hex'])
    await sparky._on_event(conduit_mock, msg)


async def test_on_setup_mode(app, mocker, conduit_mock, sparky):
    service_status.set_connected(app, 'addr')
    assert service_status.desc(app).device_address == 'addr'

    mocker.patch(TESTED + '.web.GracefulExit', RuntimeError)
    with pytest.raises(RuntimeError):
        await sparky._on_event(conduit_mock, const.SETUP_MODE_PREFIX)


async def test_on_update(app, mocker, conduit_mock, sparky):
    service_status.set_connected(app, 'addr')
    assert service_status.desc(app).device_address == 'addr'

    await sparky._on_event(conduit_mock, const.UPDATER_PREFIX + '-message')


async def test_command(conduit_mock, sparky, reset_msgid):
    await sparky._on_data(conduit_mock, '01 00 07 28 | 00 00 00')

    command = commands.ListStoredObjectsCommand.from_args()
    v = command.encoded_request
    print(v)
    resp = await sparky.execute(command)
    assert resp['objects'] == []

    conduit_mock.write.assert_called_once_with('01000728')


async def test_error_command(conduit_mock, sparky, reset_msgid):
    command = commands.ListStoredObjectsCommand.from_args()
    await sparky._on_data(conduit_mock, '01 00 07 28 | FF 00 ')

    with pytest.raises(exceptions.CommandException):
        await sparky.execute(command)


async def test_timeout_command(conduit_mock, sparky, mocker):
    mocker.patch.object(sparky, '_timeout', 0.001)
    with pytest.raises(exceptions.CommandTimeout):
        await sparky.execute(commands.ListStoredObjectsCommand.from_args())


async def test_stale_reply(conduit_mock, sparky, reset_msgid):
    # error code
    stale = commander.TimestampedResponse('ff0000')
    stale._timestamp -= timedelta(minutes=1)
    fresh = commander.TimestampedResponse('000000')

    q = sparky._requests['01000728'].queue
    await q.put(stale)
    await q.put(fresh)

    command = commands.ListStoredObjectsCommand.from_args()
    assert await sparky.execute(command)


async def test_timestamped_queue():
    q = commander.TimestampedQueue()
    assert q.fresh

    q._timestamp -= 2*commander.QUEUE_VALID_DURATION
    assert not q.fresh

    # retrieving the queue should reset timestamp
    assert q.queue.empty()
    assert q.fresh


async def test_timestamped_response():
    res = commander.TimestampedResponse('data')
    assert res.fresh

    res._timestamp -= 2*commander.RESPONSE_VALID_DURATION
    assert not res.fresh

    # retrieving data does not reset timestamp
    assert res.content == 'data'
    assert not res.fresh


async def test_queue_cleanup(mocker, conduit_mock, sparky, app):
    mocker.patch(TESTED + '.CLEANUP_INTERVAL', timedelta(milliseconds=10))
    fresh_mock = PropertyMock(return_value=True)
    type(commander.TimestampedQueue()).fresh = fresh_mock

    await sparky.startup(app)
    await sparky._on_data(conduit_mock, '05 00 |00 00 00')

    # Still fresh
    await asyncio.sleep(0.1)
    assert len(sparky._requests) == 1

    # Assert stale was removed
    fresh_mock.return_value = False
    await asyncio.sleep(0.1)
    assert len(sparky._requests) == 0


async def test_start_update(mocker, conduit_mock, sparky, app, reset_msgid):

    await sparky._on_data(conduit_mock, '01 00 64 AF |00 00 00')
    await sparky.start_update(0.001)
    conduit_mock.shutdown.assert_awaited()

    with pytest.raises(exceptions.UpdateInProgress):
        await sparky.execute(commands.ListStoredObjectsCommand.from_args())

"""
Tests brewblox_devcon_spark.global_store
"""


import pytest
from aiohttp import web
from aresponses import ResponsesMockServer
from brewblox_service import http, scheduler
from unittest.mock import AsyncMock

from brewblox_devcon_spark import const, global_store
from brewblox_devcon_spark.global_store import GlobalConfigStore

TESTED = global_store.__name__


def add_read_resp(aresponses: ResponsesMockServer, count, status=200):
    async def handler(request):
        return web.json_response({
            'values': [{
                'id': const.GLOBAL_UNITS_ID,
                'namespace': const.GLOBAL_NAMESPACE,
                'temperature': 'degF',
            }]
        },
            status=status)
    aresponses.add(path_pattern='/history/datastore/mget',
                   method_pattern='POST',
                   response=handler,
                   repeat=count)


@pytest.fixture(autouse=True)
def m_mqtt(mocker):
    m = mocker.patch(TESTED + '.mqtt')
    m.listen = AsyncMock()
    m.subscribe = AsyncMock()
    m.unlisten = AsyncMock()
    m.unsubscribe = AsyncMock()
    return m


@pytest.fixture
def app(app):
    app['config']['volatile'] = False
    http.setup(app)
    scheduler.setup(app)
    global_store.setup(app)
    return app


@pytest.fixture
def store(app):
    return global_store.fget(app)


async def test_read(app, client, store: GlobalConfigStore, aresponses):
    add_read_resp(aresponses, 1)

    await store.read()
    assert store.units['temperature'] == 'degF'
    aresponses.assert_plan_strictly_followed()


async def test_read_error(app, client, store: GlobalConfigStore, aresponses):
    add_read_resp(aresponses, 1, 405)

    await store.read()
    assert store.units['temperature'] == 'degC'
    aresponses.assert_plan_strictly_followed()


async def test_on_event(app, client, store: GlobalConfigStore):
    cb = AsyncMock()
    store.listeners.add(cb)

    # Empty
    await store._on_event('topic', {})
    assert store.units['temperature'] == 'degC'
    cb.assert_not_awaited()

    # Unrelated
    await store._on_event('topic', {'changed': [{
        'id': 'imperialist_units',
        'namespace': const.GLOBAL_NAMESPACE,
        'temperature': 'degF',
    }]})
    assert store.units['temperature'] == 'degC'
    cb.assert_not_awaited()

    # Same
    await store._on_event('topic', {'changed': [{
        'id': const.GLOBAL_UNITS_ID,
        'namespace': const.GLOBAL_NAMESPACE,
        'temperature': 'degC',
    }]})
    assert store.units['temperature'] == 'degC'
    cb.assert_not_awaited()

    # Units changed
    cb.reset_mock()
    await store._on_event('topic', {'changed': [{
        'id': const.GLOBAL_UNITS_ID,
        'namespace': const.GLOBAL_NAMESPACE,
        'temperature': 'degF',
    }]})
    assert store.units['temperature'] == 'degF'
    cb.assert_awaited_with()

    # Timezone changed
    cb.reset_mock()
    await store._on_event('topic', {'changed': [{
        'id': const.GLOBAL_TIME_ZONE_ID,
        'namespace': const.GLOBAL_NAMESPACE,
        'name': 'Europe/Amsterdam',
        'posixValue': 'CET-1CEST,M3.5.0,M10.5.0/3',
    }]})
    assert store.time_zone['name'] == 'Europe/Amsterdam'
    cb.assert_awaited_with()

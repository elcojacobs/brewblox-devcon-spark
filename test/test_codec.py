"""
Tests brewblox codec
"""

from contextlib import asynccontextmanager

import pytest
from fastapi import FastAPI

from brewblox_devcon_spark import codec, connection, exceptions
from brewblox_devcon_spark.codec import (Codec, DecodeOpts, MetadataOpt,
                                         ProtoEnumOpt)
from brewblox_devcon_spark.models import (DecodedPayload, EncodedPayload,
                                          MaskMode)

TEMP_SENSOR_TYPE_INT = 302


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with connection.lifespan():
        yield


@pytest.fixture(autouse=True)
def app() -> FastAPI:
    # state_machine.setup()
    codec.setup()
    # connection.setup(app)
    return FastAPI()


async def test_type_conversion():
    for (joined, split) in [
        ['Pid', ('Pid', None)],
        ['Pid.subtype', ('Pid', 'subtype')],
        ['Pid.subtype.subsubtype', ('Pid', 'subtype.subsubtype')]
    ]:
        assert codec.split_type(joined) == split
        assert codec.join_type(*split) == joined


async def test_encode_system_objects():
    cdc = codec.CV.get()

    types = [
        'SysInfo',
        'OneWireBus',
    ]

    encoded = [
        cdc.encode_payload(DecodedPayload(
            blockId=1,
            blockType=t,
            content={},
        ))
        for t in types]

    assert encoded


async def test_encode_errors():
    cdc = codec.CV.get()

    with pytest.raises(exceptions.EncodeException):
        cdc.encode_request({})

    with pytest.raises(exceptions.EncodeException):
        cdc.encode_response({})

    with pytest.raises(exceptions.EncodeException):
        cdc.encode_payload(DecodedPayload(
            blockId=1,
            blockType='MAGIC'
        ))

    with pytest.raises(exceptions.EncodeException):
        cdc.encode_payload(DecodedPayload(
            blockId=1,
            blockType='TempSensorOneWire',
            content={'Galileo': 'thunderbolts and lightning'}
        ))


async def test_decode_errors():
    cdc = codec.CV.get()

    with pytest.raises(exceptions.DecodeException):
        cdc.decode_request('Is this just fantasy?')

    with pytest.raises(exceptions.DecodeException):
        cdc.decode_response('Caught in a landslide')

    error_object = cdc.decode_payload(EncodedPayload(
        blockId=1,
        blockType=TEMP_SENSOR_TYPE_INT,
        content='Galileo, Figaro - magnificoo',
    ))
    assert error_object.blockType == 'ErrorObject'
    assert error_object.content['error']

    error_object = cdc.decode_payload(EncodedPayload(
        blockId=1,
        blockType=1e6,
    ))
    assert error_object.blockType == 'UnknownType'


async def test_deprecated_object():
    cdc = codec.CV.get()

    payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='DeprecatedObject',
        content={'actualId': 100},
    ))
    assert payload.blockType == 65533
    assert payload.content == 'ZAA='

    payload = cdc.decode_payload(payload)
    assert payload.blockType == 'DeprecatedObject'
    assert payload.content == {'actualId': 100}


async def test_encode_constraint():
    cdc = codec.CV.get()

    assert cdc.decode_payload(EncodedPayload(
        blockId=1,
        blockType='ActuatorPwm',
        content='\x00',
    ))
    assert cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='ActuatorPwm',
        content={
            'constrainedBy': {
                'constraints': [
                    {'min': -100},
                    {'max': 100},
                ],
            },
        },
    ))


async def test_encode_delta_sec():
    cdc = codec.CV.get()

    # Check whether [delta_temperature / time] can be converted
    payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='EdgeCase',
        content={'deltaV': 100}
    ))
    payload = cdc.decode_payload(payload, opts=DecodeOpts(metadata=MetadataOpt.POSTFIX))
    assert payload.content['deltaV[delta_degC / second]'] == pytest.approx(100, 0.1)


async def test_encode_submessage():
    cdc = codec.CV.get()

    payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='EdgeCase',
        subtype='SubCase',
        content={}
    ))
    assert payload.blockType == 9001
    assert payload.subtype == 1

    payload = cdc.decode_payload(payload)
    assert payload.blockType == 'EdgeCase'
    assert payload.subtype == 'SubCase'

    # Interface encoding
    payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='EdgeCase',
    ))
    assert payload.blockType == 9001

    payload = cdc.decode_payload(payload)
    assert payload.blockType == 'EdgeCase'


async def test_transcode_interfaces():
    cdc = codec.CV.get()

    for type in [
        'EdgeCase',
        'BalancerInterface',
        'SetpointSensorPair',
        'SetpointSensorPairInterface',
    ]:
        payload = cdc.encode_payload(DecodedPayload(
            blockId=1,
            blockType=type,
        ))
        payload = cdc.decode_payload(payload)
        assert payload.blockType == type


async def test_exclusive_mask():
    cdc = codec.CV.get()
    rw_cdc = Codec(strip_readonly=False)

    enc_payload = rw_cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='EdgeCase',
        content={
            'deltaV': 100,  # tag 6
            'logged': 10,  # tag 7
        },
        maskMode=MaskMode.EXCLUSIVE,
        mask=[6],
    ))
    payload = cdc.decode_payload(enc_payload)

    assert payload.content['deltaV']['value'] is None
    assert payload.content['deltaV']['unit'] == 'delta_degC / second'
    assert payload.content['logged'] == 10
    assert payload.maskMode == MaskMode.EXCLUSIVE
    assert payload.mask == [6]

    payload = cdc.decode_payload(enc_payload, opts=DecodeOpts(metadata=MetadataOpt.POSTFIX))
    assert payload.content['deltaV[delta_degC / second]'] is None


async def test_postfixed_decoding():
    cdc = codec.CV.get()

    payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='EdgeCase',
        content={
            'link': 10,
            'state': {
                'value[degC]': 10
            }
        },
    ))
    payload = cdc.decode_payload(payload, opts=DecodeOpts(metadata=MetadataOpt.POSTFIX))
    assert payload.content['link<ActuatorAnalogInterface>'] == 10
    assert payload.content['state']['value[degC]'] == pytest.approx(10, 0.01)


async def test_ipv4_encoding():
    cdc = codec.CV.get()

    payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='EdgeCase',
        content={
            'ip': '192.168.0.1'
        },
    ))
    payload = cdc.decode_payload(payload)
    assert payload.content['ip'] == '192.168.0.1'


async def test_point_presence():
    cdc = codec.CV.get()

    present_payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='SetpointProfile',
        content={
            'points': [
                {'time[s]': 0, 'temperature[degC]': 0},
                {'time[s]': 10, 'temperature[degC]': 10},
            ]
        },
    ))

    absent_payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='SetpointProfile',
        content={
            'points': [
                {'time[s]': 10, 'temperature[degC]': 10},
            ]
        },
    ))

    assert present_payload.content != absent_payload.content

    present_payload = cdc.decode_payload(present_payload)
    absent_payload = cdc.decode_payload(absent_payload)
    assert present_payload.content['points'][0]['time']['value'] == 0


async def test_enum_decoding():
    cdc = codec.CV.get()

    encoded_payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='DigitalActuator',
        content={
            'storedState': 'STATE_ACTIVE',
        },
    ))

    encoded_int_payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='DigitalActuator',
        content={
            'storedState': 1,
        },
    ))

    # String and int enums are both valid input
    assert encoded_payload.content == encoded_int_payload.content

    payload = cdc.decode_payload(encoded_payload)
    assert payload.content['storedState'] == 'STATE_ACTIVE'

    payload = cdc.decode_payload(encoded_payload, opts=DecodeOpts(enums=ProtoEnumOpt.INT))
    assert payload.content['storedState'] == 1


async def test_invalid_if_decoding():
    cdc = codec.CV.get()

    encoded_payload = cdc.encode_payload(DecodedPayload(
        blockId=1,
        blockType='EdgeCase',
        content={
            'listValues': [0, 10],  # omit if zero
            'deltaV': 0,  # null if zero
            'logged': 0,  # omit if zero
        },
    ))

    payload = cdc.decode_payload(encoded_payload)
    assert len(payload.content['listValues']) == 1
    assert payload.content['listValues'][0]['value'] == pytest.approx(10)
    assert payload.content['deltaV']['value'] is None
    assert 'logged' not in payload.content

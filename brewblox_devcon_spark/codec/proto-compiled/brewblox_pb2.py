# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: brewblox.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='brewblox.proto',
  package='brewblox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x62rewblox.proto\x12\x08\x62rewblox\x1a google/protobuf/descriptor.proto\x1a\x0cnanopb.proto\"|\n\x0bMessageOpts\x12$\n\x07objtype\x18\x03 \x01(\x0e\x32\x13.brewblox.BlockType\x12(\n\x04impl\x18\t \x03(\x0e\x32\x13.brewblox.BlockTypeB\x05\x92?\x02\x10\x05\x12\x16\n\x07subtype\x18\x0b \x01(\rB\x05\x92?\x02\x38\x10:\x05\x92?\x02\x30\x01\"\xdd\x01\n\tFieldOpts\x12 \n\x04unit\x18\x01 \x01(\x0e\x32\x12.brewblox.UnitType\x12\r\n\x05scale\x18\x02 \x01(\r\x12$\n\x07objtype\x18\x03 \x01(\x0e\x32\x13.brewblox.BlockType\x12\r\n\x05hexed\x18\x04 \x01(\x08\x12\x10\n\x08readonly\x18\x05 \x01(\x08\x12\x0e\n\x06logged\x18\x06 \x01(\x08\x12\x0e\n\x06hexstr\x18\x07 \x01(\x08\x12\x0e\n\x06\x64riven\x18\x08 \x01(\x08\x12\x0f\n\x07ignored\x18\t \x01(\x08\x12\x10\n\x08\x62itfield\x18\n \x01(\x08:\x05\x92?\x02\x30\x01*\x8c\x02\n\x08UnitType\x12\n\n\x06NotSet\x10\x00\x12\x0b\n\x07\x43\x65lsius\x10\x01\x12\x12\n\x0eInverseCelsius\x10\x02\x12\n\n\x06Second\x10\x03\x12\n\n\x06Minute\x10\x04\x12\x08\n\x04Hour\x10\x05\x12\x10\n\x0c\x44\x65ltaCelsius\x10\x06\x12\x19\n\x15\x44\x65ltaCelsiusPerSecond\x10\x07\x12\x19\n\x15\x44\x65ltaCelsiusPerMinute\x10\x08\x12\x17\n\x13\x44\x65ltaCelsiusPerHour\x10\t\x12\x1a\n\x16\x44\x65ltaCelsiusMultSecond\x10\n\x12\x1a\n\x16\x44\x65ltaCelsiusMultMinute\x10\x0b\x12\x18\n\x14\x44\x65ltaCelsiusMultHour\x10\x0c*\xaf\x07\n\tBlockType\x12\x0b\n\x07Invalid\x10\x00\x12\x19\n\x15ProcessValueInterface\x10\x01\x12\x17\n\x13TempSensorInterface\x10\x02\x12\x1f\n\x1bSetpointSensorPairInterface\x10\x04\x12\x1b\n\x17\x41\x63tuatorAnalogInterface\x10\x05\x12\x1c\n\x18\x41\x63tuatorDigitalInterface\x10\x06\x12\x15\n\x11\x42\x61lancerInterface\x10\x07\x12\x12\n\x0eMutexInterface\x10\x08\x12\x1a\n\x16OneWireDeviceInterface\x10\t\x12\x14\n\x10IoArrayInterface\x10\n\x12\x13\n\x0f\x44S2408Interface\x10\x0b\x12\x17\n\x13OneWireBusInterface\x10\x0c\x12\x15\n\x11IoModuleInterface\x10\r\x12\x1f\n\x1bOneWireDeviceBlockInterface\x10\x0e\x12\x14\n\x10\x45nablerInterface\x10\x0f\x12\x08\n\x03\x41ny\x10\xff\x01\x12\x0c\n\x07SysInfo\x10\x80\x02\x12\n\n\x05Ticks\x10\x81\x02\x12\x0f\n\nOneWireBus\x10\x82\x02\x12\x0e\n\tBoardPins\x10\x83\x02\x12\x13\n\x0eTempSensorMock\x10\xad\x02\x12\x16\n\x11TempSensorOneWire\x10\xae\x02\x12\x17\n\x12SetpointSensorPair\x10\xaf\x02\x12\x08\n\x03Pid\x10\xb0\x02\x12\x17\n\x12\x41\x63tuatorAnalogMock\x10\xb1\x02\x12\x10\n\x0b\x41\x63tuatorPin\x10\xb2\x02\x12\x10\n\x0b\x41\x63tuatorPwm\x10\xb3\x02\x12\x13\n\x0e\x41\x63tuatorOffset\x10\xb4\x02\x12\r\n\x08\x42\x61lancer\x10\xb5\x02\x12\n\n\x05Mutex\x10\xb6\x02\x12\x14\n\x0fSetpointProfile\x10\xb7\x02\x12\x11\n\x0cWiFiSettings\x10\xb8\x02\x12\x12\n\rTouchSettings\x10\xb9\x02\x12\x14\n\x0f\x44isplaySettings\x10\xba\x02\x12\x0b\n\x06\x44S2413\x10\xbb\x02\x12\x14\n\x0f\x41\x63tuatorOneWire\x10\xbc\x02\x12\x0b\n\x06\x44S2408\x10\xbd\x02\x12\x14\n\x0f\x44igitalActuator\x10\xbe\x02\x12\x0f\n\nSpark3Pins\x10\xbf\x02\x12\x0f\n\nSpark2Pins\x10\xc0\x02\x12\x0f\n\nMotorValve\x10\xc1\x02\x12\x12\n\rActuatorLogic\x10\xc2\x02\x12\r\n\x08MockPins\x10\xc3\x02\x12\x14\n\x0fTempSensorCombi\x10\xc4\x02\x12\x16\n\x11OneWireGpioModule\x10\xc5\x02\x12\r\n\x08Sequence\x10\xc6\x02:J\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x0b\x32\x13.brewblox.FieldOptsB\x05\x92?\x02\x18\x03:L\n\x03msg\x12\x1f.google.protobuf.MessageOptions\x18\xd1\x86\x03 \x01(\x0b\x32\x15.brewblox.MessageOptsB\x05\x92?\x02\x18\x03\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])

_UNITTYPE = _descriptor.EnumDescriptor(
  name='UnitType',
  full_name='brewblox.UnitType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NotSet', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Celsius', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InverseCelsius', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Second', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Minute', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Hour', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaCelsius', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaCelsiusPerSecond', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaCelsiusPerMinute', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaCelsiusPerHour', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaCelsiusMultSecond', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaCelsiusMultMinute', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaCelsiusMultHour', index=12, number=12,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=427,
  serialized_end=695,
)
_sym_db.RegisterEnumDescriptor(_UNITTYPE)

UnitType = enum_type_wrapper.EnumTypeWrapper(_UNITTYPE)
_BLOCKTYPE = _descriptor.EnumDescriptor(
  name='BlockType',
  full_name='brewblox.BlockType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Invalid', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProcessValueInterface', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TempSensorInterface', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetpointSensorPairInterface', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorAnalogInterface', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorDigitalInterface', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BalancerInterface', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MutexInterface', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWireDeviceInterface', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IoArrayInterface', index=9, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS2408Interface', index=10, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWireBusInterface', index=11, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IoModuleInterface', index=12, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWireDeviceBlockInterface', index=13, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EnablerInterface', index=14, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Any', index=15, number=255,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SysInfo', index=16, number=256,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ticks', index=17, number=257,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWireBus', index=18, number=258,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BoardPins', index=19, number=259,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TempSensorMock', index=20, number=301,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TempSensorOneWire', index=21, number=302,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetpointSensorPair', index=22, number=303,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pid', index=23, number=304,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorAnalogMock', index=24, number=305,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorPin', index=25, number=306,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorPwm', index=26, number=307,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorOffset', index=27, number=308,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Balancer', index=28, number=309,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Mutex', index=29, number=310,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetpointProfile', index=30, number=311,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WiFiSettings', index=31, number=312,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TouchSettings', index=32, number=313,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DisplaySettings', index=33, number=314,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS2413', index=34, number=315,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorOneWire', index=35, number=316,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS2408', index=36, number=317,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DigitalActuator', index=37, number=318,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Spark3Pins', index=38, number=319,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Spark2Pins', index=39, number=320,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MotorValve', index=40, number=321,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorLogic', index=41, number=322,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MockPins', index=42, number=323,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TempSensorCombi', index=43, number=324,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWireGpioModule', index=44, number=325,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Sequence', index=45, number=326,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=698,
  serialized_end=1641,
)
_sym_db.RegisterEnumDescriptor(_BLOCKTYPE)

BlockType = enum_type_wrapper.EnumTypeWrapper(_BLOCKTYPE)
NotSet = 0
Celsius = 1
InverseCelsius = 2
Second = 3
Minute = 4
Hour = 5
DeltaCelsius = 6
DeltaCelsiusPerSecond = 7
DeltaCelsiusPerMinute = 8
DeltaCelsiusPerHour = 9
DeltaCelsiusMultSecond = 10
DeltaCelsiusMultMinute = 11
DeltaCelsiusMultHour = 12
Invalid = 0
ProcessValueInterface = 1
TempSensorInterface = 2
SetpointSensorPairInterface = 4
ActuatorAnalogInterface = 5
ActuatorDigitalInterface = 6
BalancerInterface = 7
MutexInterface = 8
OneWireDeviceInterface = 9
IoArrayInterface = 10
DS2408Interface = 11
OneWireBusInterface = 12
IoModuleInterface = 13
OneWireDeviceBlockInterface = 14
EnablerInterface = 15
Any = 255
SysInfo = 256
Ticks = 257
OneWireBus = 258
BoardPins = 259
TempSensorMock = 301
TempSensorOneWire = 302
SetpointSensorPair = 303
Pid = 304
ActuatorAnalogMock = 305
ActuatorPin = 306
ActuatorPwm = 307
ActuatorOffset = 308
Balancer = 309
Mutex = 310
SetpointProfile = 311
WiFiSettings = 312
TouchSettings = 313
DisplaySettings = 314
DS2413 = 315
ActuatorOneWire = 316
DS2408 = 317
DigitalActuator = 318
Spark3Pins = 319
Spark2Pins = 320
MotorValve = 321
ActuatorLogic = 322
MockPins = 323
TempSensorCombi = 324
OneWireGpioModule = 325
Sequence = 326

FIELD_FIELD_NUMBER = 50001
field = _descriptor.FieldDescriptor(
  name='field', full_name='brewblox.field', index=0,
  number=50001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=_b('\222?\002\030\003'), file=DESCRIPTOR)
MSG_FIELD_NUMBER = 50001
msg = _descriptor.FieldDescriptor(
  name='msg', full_name='brewblox.msg', index=1,
  number=50001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=_b('\222?\002\030\003'), file=DESCRIPTOR)


_MESSAGEOPTS = _descriptor.Descriptor(
  name='MessageOpts',
  full_name='brewblox.MessageOpts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objtype', full_name='brewblox.MessageOpts.objtype', index=0,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='impl', full_name='brewblox.MessageOpts.impl', index=1,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\002\020\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='brewblox.MessageOpts.subtype', index=2,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\020'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\222?\0020\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=200,
)


_FIELDOPTS = _descriptor.Descriptor(
  name='FieldOpts',
  full_name='brewblox.FieldOpts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit', full_name='brewblox.FieldOpts.unit', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='brewblox.FieldOpts.scale', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objtype', full_name='brewblox.FieldOpts.objtype', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hexed', full_name='brewblox.FieldOpts.hexed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readonly', full_name='brewblox.FieldOpts.readonly', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logged', full_name='brewblox.FieldOpts.logged', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hexstr', full_name='brewblox.FieldOpts.hexstr', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='driven', full_name='brewblox.FieldOpts.driven', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignored', full_name='brewblox.FieldOpts.ignored', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bitfield', full_name='brewblox.FieldOpts.bitfield', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\222?\0020\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=424,
)

_MESSAGEOPTS.fields_by_name['objtype'].enum_type = _BLOCKTYPE
_MESSAGEOPTS.fields_by_name['impl'].enum_type = _BLOCKTYPE
_FIELDOPTS.fields_by_name['unit'].enum_type = _UNITTYPE
_FIELDOPTS.fields_by_name['objtype'].enum_type = _BLOCKTYPE
DESCRIPTOR.message_types_by_name['MessageOpts'] = _MESSAGEOPTS
DESCRIPTOR.message_types_by_name['FieldOpts'] = _FIELDOPTS
DESCRIPTOR.enum_types_by_name['UnitType'] = _UNITTYPE
DESCRIPTOR.enum_types_by_name['BlockType'] = _BLOCKTYPE
DESCRIPTOR.extensions_by_name['field'] = field
DESCRIPTOR.extensions_by_name['msg'] = msg
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageOpts = _reflection.GeneratedProtocolMessageType('MessageOpts', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEOPTS,
  __module__ = 'brewblox_pb2'
  # @@protoc_insertion_point(class_scope:brewblox.MessageOpts)
  ))
_sym_db.RegisterMessage(MessageOpts)

FieldOpts = _reflection.GeneratedProtocolMessageType('FieldOpts', (_message.Message,), dict(
  DESCRIPTOR = _FIELDOPTS,
  __module__ = 'brewblox_pb2'
  # @@protoc_insertion_point(class_scope:brewblox.FieldOpts)
  ))
_sym_db.RegisterMessage(FieldOpts)

field.message_type = _FIELDOPTS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field)
msg.message_type = _MESSAGEOPTS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(msg)

field._options = None
msg._options = None
_MESSAGEOPTS.fields_by_name['impl']._options = None
_MESSAGEOPTS.fields_by_name['subtype']._options = None
_MESSAGEOPTS._options = None
_FIELDOPTS._options = None
# @@protoc_insertion_point(module_scope)

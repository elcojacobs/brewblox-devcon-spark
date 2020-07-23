# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: brewblox.proto

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
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0e\x62rewblox.proto\x1a google/protobuf/descriptor.proto\x1a\x0cnanopb.proto\"\xac\x08\n\rBrewBloxTypes\"\x8c\x02\n\x08UnitType\x12\n\n\x06NotSet\x10\x00\x12\x0b\n\x07\x43\x65lsius\x10\x01\x12\x12\n\x0eInverseCelsius\x10\x02\x12\n\n\x06Second\x10\x03\x12\n\n\x06Minute\x10\x04\x12\x08\n\x04Hour\x10\x05\x12\x10\n\x0c\x44\x65ltaCelsius\x10\x06\x12\x19\n\x15\x44\x65ltaCelsiusPerSecond\x10\x07\x12\x19\n\x15\x44\x65ltaCelsiusPerMinute\x10\x08\x12\x17\n\x13\x44\x65ltaCelsiusPerHour\x10\t\x12\x1a\n\x16\x44\x65ltaCelsiusMultSecond\x10\n\x12\x1a\n\x16\x44\x65ltaCelsiusMultMinute\x10\x0b\x12\x18\n\x14\x44\x65ltaCelsiusMultHour\x10\x0c\"\x8b\x06\n\tBlockType\x12\x0b\n\x07Invalid\x10\x00\x12\x19\n\x15ProcessValueInterface\x10\x01\x12\x17\n\x13TempSensorInterface\x10\x02\x12\x1f\n\x1bSetpointSensorPairInterface\x10\x04\x12\x1b\n\x17\x41\x63tuatorAnalogInterface\x10\x05\x12\x1c\n\x18\x41\x63tuatorDigitalInterface\x10\x06\x12\x15\n\x11\x42\x61lancerInterface\x10\x07\x12\x12\n\x0eMutexInterface\x10\x08\x12\x1a\n\x16OneWireDeviceInterface\x10\t\x12\x14\n\x10IoArrayInterface\x10\n\x12\x13\n\x0f\x44S2408Interface\x10\x0b\x12\x08\n\x03\x41ny\x10\xff\x01\x12\x0c\n\x07SysInfo\x10\x80\x02\x12\n\n\x05Ticks\x10\x81\x02\x12\x0f\n\nOneWireBus\x10\x82\x02\x12\x0e\n\tBoardPins\x10\x83\x02\x12\x13\n\x0eTempSensorMock\x10\xad\x02\x12\x16\n\x11TempSensorOneWire\x10\xae\x02\x12\x17\n\x12SetpointSensorPair\x10\xaf\x02\x12\x08\n\x03Pid\x10\xb0\x02\x12\x17\n\x12\x41\x63tuatorAnalogMock\x10\xb1\x02\x12\x10\n\x0b\x41\x63tuatorPin\x10\xb2\x02\x12\x10\n\x0b\x41\x63tuatorPwm\x10\xb3\x02\x12\x13\n\x0e\x41\x63tuatorOffset\x10\xb4\x02\x12\r\n\x08\x42\x61lancer\x10\xb5\x02\x12\n\n\x05Mutex\x10\xb6\x02\x12\x14\n\x0fSetpointProfile\x10\xb7\x02\x12\x11\n\x0cWiFiSettings\x10\xb8\x02\x12\x12\n\rTouchSettings\x10\xb9\x02\x12\x14\n\x0f\x44isplaySettings\x10\xba\x02\x12\x0b\n\x06\x44S2413\x10\xbb\x02\x12\x14\n\x0f\x41\x63tuatorOneWire\x10\xbc\x02\x12\x0b\n\x06\x44S2408\x10\xbd\x02\x12\x14\n\x0f\x44igitalActuator\x10\xbe\x02\x12\x0f\n\nSpark3Pins\x10\xbf\x02\x12\x0f\n\nSpark2Pins\x10\xc0\x02\x12\x0f\n\nMotorValve\x10\xc1\x02\x12\x12\n\rActuatorLogic\x10\xc2\x02\x12\r\n\x08MockPins\x10\xc3\x02\"y\n\x16\x42rewBloxMessageOptions\x12)\n\x07objtype\x18\x03 \x01(\x0e\x32\x18.BrewBloxTypes.BlockType\x12-\n\x04impl\x18\t \x03(\x0e\x32\x18.BrewBloxTypes.BlockTypeB\x05\x92?\x02\x10\x05:\x05\x92?\x02\x30\x01\"\xe0\x01\n\x14\x42rewBloxFieldOptions\x12%\n\x04unit\x18\x01 \x01(\x0e\x32\x17.BrewBloxTypes.UnitType\x12\r\n\x05scale\x18\x02 \x01(\r\x12)\n\x07objtype\x18\x03 \x01(\x0e\x32\x18.BrewBloxTypes.BlockType\x12\r\n\x05hexed\x18\x04 \x01(\x08\x12\x10\n\x08readonly\x18\x05 \x01(\x08\x12\x0e\n\x06logged\x18\x06 \x01(\x08\x12\x0e\n\x06hexstr\x18\x07 \x01(\x08\x12\x0e\n\x06\x64riven\x18\x08 \x01(\x08\x12\x0f\n\x07ignored\x18\t \x01(\x08:\x05\x92?\x02\x30\x01:O\n\x08\x62rewblox\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x0b\x32\x15.BrewBloxFieldOptionsB\x05\x92?\x02\x18\x03:W\n\x0c\x62rewblox_msg\x12\x1f.google.protobuf.MessageOptions\x18\xd1\x86\x03 \x01(\x0b\x32\x17.BrewBloxMessageOptionsB\x05\x92?\x02\x18\x03'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])


BREWBLOX_FIELD_NUMBER = 50001
brewblox = _descriptor.FieldDescriptor(
  name='brewblox', full_name='brewblox', index=0,
  number=50001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=b'\222?\002\030\003', file=DESCRIPTOR)
BREWBLOX_MSG_FIELD_NUMBER = 50001
brewblox_msg = _descriptor.FieldDescriptor(
  name='brewblox_msg', full_name='brewblox_msg', index=1,
  number=50001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=b'\222?\002\030\003', file=DESCRIPTOR)

_BREWBLOXTYPES_UNITTYPE = _descriptor.EnumDescriptor(
  name='UnitType',
  full_name='BrewBloxTypes.UnitType',
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
  serialized_start=85,
  serialized_end=353,
)
_sym_db.RegisterEnumDescriptor(_BREWBLOXTYPES_UNITTYPE)

_BREWBLOXTYPES_BLOCKTYPE = _descriptor.EnumDescriptor(
  name='BlockType',
  full_name='BrewBloxTypes.BlockType',
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
      name='Any', index=11, number=255,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SysInfo', index=12, number=256,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ticks', index=13, number=257,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWireBus', index=14, number=258,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BoardPins', index=15, number=259,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TempSensorMock', index=16, number=301,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TempSensorOneWire', index=17, number=302,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetpointSensorPair', index=18, number=303,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pid', index=19, number=304,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorAnalogMock', index=20, number=305,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorPin', index=21, number=306,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorPwm', index=22, number=307,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorOffset', index=23, number=308,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Balancer', index=24, number=309,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Mutex', index=25, number=310,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetpointProfile', index=26, number=311,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WiFiSettings', index=27, number=312,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TouchSettings', index=28, number=313,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DisplaySettings', index=29, number=314,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS2413', index=30, number=315,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorOneWire', index=31, number=316,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS2408', index=32, number=317,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DigitalActuator', index=33, number=318,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Spark3Pins', index=34, number=319,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Spark2Pins', index=35, number=320,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MotorValve', index=36, number=321,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorLogic', index=37, number=322,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MockPins', index=38, number=323,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=356,
  serialized_end=1135,
)
_sym_db.RegisterEnumDescriptor(_BREWBLOXTYPES_BLOCKTYPE)


_BREWBLOXTYPES = _descriptor.Descriptor(
  name='BrewBloxTypes',
  full_name='BrewBloxTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BREWBLOXTYPES_UNITTYPE,
    _BREWBLOXTYPES_BLOCKTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=1135,
)


_BREWBLOXMESSAGEOPTIONS = _descriptor.Descriptor(
  name='BrewBloxMessageOptions',
  full_name='BrewBloxMessageOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objtype', full_name='BrewBloxMessageOptions.objtype', index=0,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='impl', full_name='BrewBloxMessageOptions.impl', index=1,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002\020\005', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\222?\0020\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1137,
  serialized_end=1258,
)


_BREWBLOXFIELDOPTIONS = _descriptor.Descriptor(
  name='BrewBloxFieldOptions',
  full_name='BrewBloxFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit', full_name='BrewBloxFieldOptions.unit', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='BrewBloxFieldOptions.scale', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objtype', full_name='BrewBloxFieldOptions.objtype', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hexed', full_name='BrewBloxFieldOptions.hexed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readonly', full_name='BrewBloxFieldOptions.readonly', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logged', full_name='BrewBloxFieldOptions.logged', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hexstr', full_name='BrewBloxFieldOptions.hexstr', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='driven', full_name='BrewBloxFieldOptions.driven', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignored', full_name='BrewBloxFieldOptions.ignored', index=8,
      number=9, type=8, cpp_type=7, label=1,
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
  serialized_options=b'\222?\0020\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1261,
  serialized_end=1485,
)

_BREWBLOXTYPES_UNITTYPE.containing_type = _BREWBLOXTYPES
_BREWBLOXTYPES_BLOCKTYPE.containing_type = _BREWBLOXTYPES
_BREWBLOXMESSAGEOPTIONS.fields_by_name['objtype'].enum_type = _BREWBLOXTYPES_BLOCKTYPE
_BREWBLOXMESSAGEOPTIONS.fields_by_name['impl'].enum_type = _BREWBLOXTYPES_BLOCKTYPE
_BREWBLOXFIELDOPTIONS.fields_by_name['unit'].enum_type = _BREWBLOXTYPES_UNITTYPE
_BREWBLOXFIELDOPTIONS.fields_by_name['objtype'].enum_type = _BREWBLOXTYPES_BLOCKTYPE
DESCRIPTOR.message_types_by_name['BrewBloxTypes'] = _BREWBLOXTYPES
DESCRIPTOR.message_types_by_name['BrewBloxMessageOptions'] = _BREWBLOXMESSAGEOPTIONS
DESCRIPTOR.message_types_by_name['BrewBloxFieldOptions'] = _BREWBLOXFIELDOPTIONS
DESCRIPTOR.extensions_by_name['brewblox'] = brewblox
DESCRIPTOR.extensions_by_name['brewblox_msg'] = brewblox_msg
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BrewBloxTypes = _reflection.GeneratedProtocolMessageType('BrewBloxTypes', (_message.Message,), {
  'DESCRIPTOR' : _BREWBLOXTYPES,
  '__module__' : 'brewblox_pb2'
  # @@protoc_insertion_point(class_scope:BrewBloxTypes)
  })
_sym_db.RegisterMessage(BrewBloxTypes)

BrewBloxMessageOptions = _reflection.GeneratedProtocolMessageType('BrewBloxMessageOptions', (_message.Message,), {
  'DESCRIPTOR' : _BREWBLOXMESSAGEOPTIONS,
  '__module__' : 'brewblox_pb2'
  # @@protoc_insertion_point(class_scope:BrewBloxMessageOptions)
  })
_sym_db.RegisterMessage(BrewBloxMessageOptions)

BrewBloxFieldOptions = _reflection.GeneratedProtocolMessageType('BrewBloxFieldOptions', (_message.Message,), {
  'DESCRIPTOR' : _BREWBLOXFIELDOPTIONS,
  '__module__' : 'brewblox_pb2'
  # @@protoc_insertion_point(class_scope:BrewBloxFieldOptions)
  })
_sym_db.RegisterMessage(BrewBloxFieldOptions)

brewblox.message_type = _BREWBLOXFIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(brewblox)
brewblox_msg.message_type = _BREWBLOXMESSAGEOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(brewblox_msg)

brewblox._options = None
brewblox_msg._options = None
_BREWBLOXMESSAGEOPTIONS.fields_by_name['impl']._options = None
_BREWBLOXMESSAGEOPTIONS._options = None
_BREWBLOXFIELDOPTIONS._options = None
# @@protoc_insertion_point(module_scope)

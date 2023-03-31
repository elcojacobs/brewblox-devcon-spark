# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SysInfo.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SysInfo.proto',
  package='blox.SysInfo',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rSysInfo.proto\x12\x0c\x62lox.SysInfo\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xf1\x05\n\x05\x42lock\x12#\n\x08\x64\x65viceId\x18\x01 \x01(\x0c\x42\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x08\x0c\x8a\xb5\x18\x02\x38\x01\x12\x1c\n\x07version\x18\x02 \x01(\tB\x0b\x8a\xb5\x18\x02(\x01\x92?\x02\x08\x0c\x12\x30\n\x08platform\x18\x03 \x01(\x0e\x32\x16.blox.SysInfo.PlatformB\x06\x8a\xb5\x18\x02(\x01\x12$\n\x0fprotocolVersion\x18\x07 \x01(\tB\x0b\x8a\xb5\x18\x02(\x01\x92?\x02\x08\x0c\x12 \n\x0breleaseDate\x18\x08 \x01(\tB\x0b\x8a\xb5\x18\x02(\x01\x92?\x02\x08\x0c\x12!\n\x0cprotocolDate\x18\t \x01(\tB\x0b\x8a\xb5\x18\x02(\x01\x92?\x02\x08\x0c\x12\x1d\n\x02ip\x18\n \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x02`\x01\x92?\x02\x38 \x12.\n\x06uptime\x18\x0b \x01(\rB\x1e\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x03\x8a\xb5\x18\x03\x10\xe8\x07\x92?\x02\x38 \x12\x32\n\x10updatesPerSecond\x18\x0c \x01(\rB\x18\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\xe8\x07\x92?\x02\x38 \x12\x1f\n\nsystemTime\x18\r \x01(\rB\x0b\x8a\xb5\x18\x02X\x01\x92?\x02\x38 \x12\x17\n\x08timeZone\x18\x0e \x01(\tB\x05\x92?\x02\x08 \x12/\n\x08tempUnit\x18\x0f \x01(\x0e\x32\x1d.blox.SysInfo.TemperatureUnit\x12 \n\x11\x64isplayBrightness\x18\x10 \x01(\rB\x05\x92?\x02\x38\x08\x12$\n\x08voltage5\x18\x11 \x01(\rB\x12\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x8a\xb5\x18\x03\x10\xe8\x07\x12+\n\x0fvoltageExternal\x18\x12 \x01(\rB\x12\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x8a\xb5\x18\x03\x10\xe8\x07\x12\x1a\n\nmemoryFree\x18\x13 \x01(\rB\x06\x8a\xb5\x18\x02(\x01\x12$\n\x14memoryFreeContiguous\x18\x14 \x01(\rB\x06\x8a\xb5\x18\x02(\x01\x12 \n\x10memoryFreeLowest\x18\x15 \x01(\rB\x06\x8a\xb5\x18\x02(\x01\x12\x1c\n\x07\x63ommand\x18Z \x01(\x08\x42\x0b\x8a\xb5\x18\x02H\x01\x92?\x02\x18\x03\x12\x1a\n\x05trace\x18[ \x01(\x08\x42\x0b\x8a\xb5\x18\x02H\x01\x92?\x02\x18\x03:\x07\x8a\xb5\x18\x03\x18\x80\x02*}\n\x08Platform\x12\x14\n\x10PLATFORM_UNKNOWN\x10\x00\x12\x10\n\x0cPLATFORM_GCC\x10\x03\x12\x13\n\x0fPLATFORM_PHOTON\x10\x06\x12\x0f\n\x0bPLATFORM_P1\x10\x08\x12\x10\n\x0cPLATFORM_ESP\x10\x64\x12\x11\n\x0cPLATFORM_SIM\x10\xc8\x01*8\n\x0fTemperatureUnit\x12\x10\n\x0cTEMP_CELSIUS\x10\x00\x12\x13\n\x0fTEMP_FAHRENHEIT\x10\x01\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])

_PLATFORM = _descriptor.EnumDescriptor(
  name='Platform',
  full_name='blox.SysInfo.Platform',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_GCC', index=1, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_PHOTON', index=2, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_P1', index=3, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_ESP', index=4, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_SIM', index=5, number=200,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=817,
  serialized_end=942,
)
_sym_db.RegisterEnumDescriptor(_PLATFORM)

Platform = enum_type_wrapper.EnumTypeWrapper(_PLATFORM)
_TEMPERATUREUNIT = _descriptor.EnumDescriptor(
  name='TemperatureUnit',
  full_name='blox.SysInfo.TemperatureUnit',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEMP_CELSIUS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEMP_FAHRENHEIT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=944,
  serialized_end=1000,
)
_sym_db.RegisterEnumDescriptor(_TEMPERATUREUNIT)

TemperatureUnit = enum_type_wrapper.EnumTypeWrapper(_TEMPERATUREUNIT)
PLATFORM_UNKNOWN = 0
PLATFORM_GCC = 3
PLATFORM_PHOTON = 6
PLATFORM_P1 = 8
PLATFORM_ESP = 100
PLATFORM_SIM = 200
TEMP_CELSIUS = 0
TEMP_FAHRENHEIT = 1



_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.SysInfo.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='blox.SysInfo.Block.deviceId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\002\010\014\212\265\030\0028\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='blox.SysInfo.Block.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\002\010\014', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='platform', full_name='blox.SysInfo.Block.platform', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocolVersion', full_name='blox.SysInfo.Block.protocolVersion', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\002\010\014', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='releaseDate', full_name='blox.SysInfo.Block.releaseDate', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\002\010\014', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocolDate', full_name='blox.SysInfo.Block.protocolDate', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\002\010\014', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='blox.SysInfo.Block.ip', index=6,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\212\265\030\002`\001\222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uptime', full_name='blox.SysInfo.Block.uptime', index=7,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\212\265\030\0020\001\212\265\030\002\010\003\212\265\030\003\020\350\007\222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updatesPerSecond', full_name='blox.SysInfo.Block.updatesPerSecond', index=8,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\212\265\030\0020\001\212\265\030\003\020\350\007\222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemTime', full_name='blox.SysInfo.Block.systemTime', index=9,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002X\001\222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeZone', full_name='blox.SysInfo.Block.timeZone', index=10,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002\010 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tempUnit', full_name='blox.SysInfo.Block.tempUnit', index=11,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='displayBrightness', full_name='blox.SysInfo.Block.displayBrightness', index=12,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voltage5', full_name='blox.SysInfo.Block.voltage5', index=13,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\020\212\265\030\003\020\350\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voltageExternal', full_name='blox.SysInfo.Block.voltageExternal', index=14,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\020\212\265\030\003\020\350\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memoryFree', full_name='blox.SysInfo.Block.memoryFree', index=15,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memoryFreeContiguous', full_name='blox.SysInfo.Block.memoryFreeContiguous', index=16,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memoryFreeLowest', full_name='blox.SysInfo.Block.memoryFreeLowest', index=17,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command', full_name='blox.SysInfo.Block.command', index=18,
      number=90, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002H\001\222?\002\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace', full_name='blox.SysInfo.Block.trace', index=19,
      number=91, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002H\001\222?\002\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\200\002',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=815,
)

_BLOCK.fields_by_name['platform'].enum_type = _PLATFORM
_BLOCK.fields_by_name['tempUnit'].enum_type = _TEMPERATUREUNIT
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.enum_types_by_name['Platform'] = _PLATFORM
DESCRIPTOR.enum_types_by_name['TemperatureUnit'] = _TEMPERATUREUNIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'SysInfo_pb2'
  # @@protoc_insertion_point(class_scope:blox.SysInfo.Block)
  })
_sym_db.RegisterMessage(Block)


_BLOCK.fields_by_name['deviceId']._options = None
_BLOCK.fields_by_name['version']._options = None
_BLOCK.fields_by_name['platform']._options = None
_BLOCK.fields_by_name['protocolVersion']._options = None
_BLOCK.fields_by_name['releaseDate']._options = None
_BLOCK.fields_by_name['protocolDate']._options = None
_BLOCK.fields_by_name['ip']._options = None
_BLOCK.fields_by_name['uptime']._options = None
_BLOCK.fields_by_name['updatesPerSecond']._options = None
_BLOCK.fields_by_name['systemTime']._options = None
_BLOCK.fields_by_name['timeZone']._options = None
_BLOCK.fields_by_name['displayBrightness']._options = None
_BLOCK.fields_by_name['voltage5']._options = None
_BLOCK.fields_by_name['voltageExternal']._options = None
_BLOCK.fields_by_name['memoryFree']._options = None
_BLOCK.fields_by_name['memoryFreeContiguous']._options = None
_BLOCK.fields_by_name['memoryFreeLowest']._options = None
_BLOCK.fields_by_name['command']._options = None
_BLOCK.fields_by_name['trace']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

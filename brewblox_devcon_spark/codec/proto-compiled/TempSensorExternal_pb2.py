# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TempSensorExternal.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TempSensorExternal.proto',
  package='blox.TempSensorExternal',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18TempSensorExternal.proto\x12\x17\x62lox.TempSensorExternal\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xd3\x01\n\x05\x42lock\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1c\n\x07timeout\x18\x02 \x01(\rB\x0b\x8a\xb5\x18\x02\x08\x03\x92?\x02\x38 \x12)\n\x07setting\x18\x03 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12,\n\x0blastUpdated\x18\x04 \x01(\rB\x17\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02X\x01\x8a\xb5\x18\x02(\x01\x92?\x02\x38 \x12-\n\x05value\x18\x05 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x8a\xb5\x18\x02(\x01\x92?\x02\x38 :\x13\x8a\xb5\x18\x03\x18\xc8\x02\x8a\xb5\x18\x02H\x02\x8a\xb5\x18\x02H\x0f\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.TempSensorExternal.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='blox.TempSensorExternal.Block.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='blox.TempSensorExternal.Block.timeout', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\003\222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setting', full_name='blox.TempSensorExternal.Block.setting', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastUpdated', full_name='blox.TempSensorExternal.Block.lastUpdated', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002X\001\212\265\030\002(\001\222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.TempSensorExternal.Block.value', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \212\265\030\002(\001\222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\310\002\212\265\030\002H\002\212\265\030\002H\017',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=295,
)

DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'TempSensorExternal_pb2'
  # @@protoc_insertion_point(class_scope:blox.TempSensorExternal.Block)
  })
_sym_db.RegisterMessage(Block)


_BLOCK.fields_by_name['timeout']._options = None
_BLOCK.fields_by_name['setting']._options = None
_BLOCK.fields_by_name['lastUpdated']._options = None
_BLOCK.fields_by_name['value']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

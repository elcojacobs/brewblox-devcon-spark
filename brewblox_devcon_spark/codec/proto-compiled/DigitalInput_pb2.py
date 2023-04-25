# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DigitalInput.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import IoArray_pb2 as IoArray__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DigitalInput.proto',
  package='blox.DigitalInput',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x44igitalInput.proto\x12\x11\x62lox.DigitalInput\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\rIoArray.proto\"\x86\x01\n\x05\x42lock\x12\x1d\n\x08hwDevice\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\n\x92?\x02\x38\x10\x12\x16\n\x07\x63hannel\x18\x02 \x01(\rB\x05\x92?\x02\x38\x08\x12\x37\n\x05state\x18\x03 \x01(\x0e\x32\x1a.blox.IoArray.DigitalStateB\x0c\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01:\r\x8a\xb5\x18\x03\x18\xca\x02\x8a\xb5\x18\x02H\x1b\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,IoArray__pb2.DESCRIPTOR,])




_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.DigitalInput.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hwDevice', full_name='blox.DigitalInput.Block.hwDevice', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\n\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='blox.DigitalInput.Block.channel', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='blox.DigitalInput.Block.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\312\002\212\265\030\002H\033',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=221,
)

_BLOCK.fields_by_name['state'].enum_type = IoArray__pb2._DIGITALSTATE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'DigitalInput_pb2'
  # @@protoc_insertion_point(class_scope:blox.DigitalInput.Block)
  })
_sym_db.RegisterMessage(Block)


_BLOCK.fields_by_name['hwDevice']._options = None
_BLOCK.fields_by_name['channel']._options = None
_BLOCK.fields_by_name['state']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

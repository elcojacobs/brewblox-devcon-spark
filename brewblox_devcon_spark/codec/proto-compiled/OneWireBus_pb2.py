# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OneWireBus.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OneWireBus.proto',
  package='blox.OneWireBus',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10OneWireBus.proto\x12\x0f\x62lox.OneWireBus\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"5\n\x07\x43ommand\x12\x15\n\x06opcode\x18\x01 \x01(\rB\x05\x92?\x02\x38\x08\x12\x13\n\x04\x64\x61ta\x18\x02 \x01(\rB\x05\x92?\x02\x38\x08\"Z\n\x05\x42lock\x12)\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x18.blox.OneWireBus.Command\x12\x1d\n\x07\x61\x64\x64ress\x18\x02 \x03(\x06\x42\x0c\x8a\xb5\x18\x02 \x01\x8a\xb5\x18\x02(\x01:\x07\x8a\xb5\x18\x03\x18\x82\x02\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='blox.OneWireBus.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opcode', full_name='blox.OneWireBus.Command.opcode', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='blox.OneWireBus.Command.data', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=120,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.OneWireBus.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='blox.OneWireBus.Block.command', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='blox.OneWireBus.Block.address', index=1,
      number=2, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002 \001\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\202\002',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=212,
)

_BLOCK.fields_by_name['command'].message_type = _COMMAND
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'OneWireBus_pb2'
  # @@protoc_insertion_point(class_scope:blox.OneWireBus.Command)
  })
_sym_db.RegisterMessage(Command)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'OneWireBus_pb2'
  # @@protoc_insertion_point(class_scope:blox.OneWireBus.Block)
  })
_sym_db.RegisterMessage(Block)


_COMMAND.fields_by_name['opcode']._options = None
_COMMAND.fields_by_name['data']._options = None
_BLOCK.fields_by_name['address']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OneWireBus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
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
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10OneWireBus.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\x93\x01\n\nOneWireBus\x12)\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x18.blox.OneWireBus.Command\x12\x1b\n\x07\x61\x64\x64ress\x18\x02 \x03(\x06\x42\n\x9a?\x02 \x01\x9a?\x02(\x01\x1a\x35\n\x07\x43ommand\x12\x15\n\x06opcode\x18\x01 \x01(\rB\x05\x92?\x02\x38\x08\x12\x13\n\x04\x64\x61ta\x18\x02 \x01(\rB\x05\x92?\x02\x38\x08:\x06\x9a?\x03\x18\x82\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_ONEWIREBUS_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='blox.OneWireBus.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opcode', full_name='blox.OneWireBus.Command.opcode', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\010'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='blox.OneWireBus.Command.data', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\010'), file=DESCRIPTOR),
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
  serialized_start=143,
  serialized_end=196,
)

_ONEWIREBUS = _descriptor.Descriptor(
  name='OneWireBus',
  full_name='blox.OneWireBus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='blox.OneWireBus.command', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='blox.OneWireBus.address', index=1,
      number=2, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\232?\002 \001\232?\002(\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ONEWIREBUS_COMMAND, ],
  enum_types=[
  ],
  serialized_options=_b('\232?\003\030\202\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=204,
)

_ONEWIREBUS_COMMAND.containing_type = _ONEWIREBUS
_ONEWIREBUS.fields_by_name['command'].message_type = _ONEWIREBUS_COMMAND
DESCRIPTOR.message_types_by_name['OneWireBus'] = _ONEWIREBUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OneWireBus = _reflection.GeneratedProtocolMessageType('OneWireBus', (_message.Message,), dict(

  Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
    DESCRIPTOR = _ONEWIREBUS_COMMAND,
    __module__ = 'OneWireBus_pb2'
    # @@protoc_insertion_point(class_scope:blox.OneWireBus.Command)
    ))
  ,
  DESCRIPTOR = _ONEWIREBUS,
  __module__ = 'OneWireBus_pb2'
  # @@protoc_insertion_point(class_scope:blox.OneWireBus)
  ))
_sym_db.RegisterMessage(OneWireBus)
_sym_db.RegisterMessage(OneWireBus.Command)


_ONEWIREBUS_COMMAND.fields_by_name['opcode']._options = None
_ONEWIREBUS_COMMAND.fields_by_name['data']._options = None
_ONEWIREBUS.fields_by_name['address']._options = None
_ONEWIREBUS._options = None
# @@protoc_insertion_point(module_scope)

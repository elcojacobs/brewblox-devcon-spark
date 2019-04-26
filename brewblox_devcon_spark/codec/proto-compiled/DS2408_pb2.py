# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DS2408.proto

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
  name='DS2408.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x44S2408.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\x96\x01\n\x06\x44S2408\x12\x17\n\x07\x61\x64\x64ress\x18\x01 \x01(\x06\x42\x06\x8a\xb5\x18\x02 \x01\x12\x16\n\x07latches\x18\x03 \x01(\rB\x05\x92?\x02\x38\x08\x12\x19\n\x04pins\x18\x04 \x01(\rB\x0b\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x12\x1c\n\x07\x63laimed\x18\x05 \x01(\rB\x0b\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x12\x19\n\tconnected\x18\x06 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01:\x07\x8a\xb5\x18\x03\x18\xbd\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_DS2408 = _descriptor.Descriptor(
  name='DS2408',
  full_name='blox.DS2408',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='blox.DS2408.address', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002 \001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latches', full_name='blox.DS2408.latches', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\010'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pins', full_name='blox.DS2408.pins', index=2,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001\222?\0028\010'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claimed', full_name='blox.DS2408.claimed', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001\222?\0028\010'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connected', full_name='blox.DS2408.connected', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\212\265\030\003\030\275\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=203,
)

DESCRIPTOR.message_types_by_name['DS2408'] = _DS2408
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DS2408 = _reflection.GeneratedProtocolMessageType('DS2408', (_message.Message,), dict(
  DESCRIPTOR = _DS2408,
  __module__ = 'DS2408_pb2'
  # @@protoc_insertion_point(class_scope:blox.DS2408)
  ))
_sym_db.RegisterMessage(DS2408)


_DS2408.fields_by_name['address']._options = None
_DS2408.fields_by_name['latches']._options = None
_DS2408.fields_by_name['pins']._options = None
_DS2408.fields_by_name['claimed']._options = None
_DS2408.fields_by_name['connected']._options = None
_DS2408._options = None
# @@protoc_insertion_point(module_scope)

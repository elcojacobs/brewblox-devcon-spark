# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TempSensorMock.proto

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
  name='TempSensorMock.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14TempSensorMock.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\x8d\x01\n\x0eTempSensorMock\x12\'\n\x05value\x18\x01 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x19\n\tconnected\x18\x03 \x01(\x08\x42\x06\x8a\xb5\x18\x02\x30\x01\x12(\n\x0estrippedFields\x18\x63 \x03(\rB\x10\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x92?\x02\x10\x01:\r\x8a\xb5\x18\x03\x18\xad\x02\x8a\xb5\x18\x02H\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_TEMPSENSORMOCK = _descriptor.Descriptor(
  name='TempSensorMock',
  full_name='blox.TempSensorMock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.TempSensorMock.value', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connected', full_name='blox.TempSensorMock.connected', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\0020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strippedFields', full_name='blox.TempSensorMock.strippedFields', index=2,
      number=99, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001\222?\0028\020\222?\002\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\212\265\030\003\030\255\002\212\265\030\002H\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=202,
)

DESCRIPTOR.message_types_by_name['TempSensorMock'] = _TEMPSENSORMOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TempSensorMock = _reflection.GeneratedProtocolMessageType('TempSensorMock', (_message.Message,), dict(
  DESCRIPTOR = _TEMPSENSORMOCK,
  __module__ = 'TempSensorMock_pb2'
  # @@protoc_insertion_point(class_scope:blox.TempSensorMock)
  ))
_sym_db.RegisterMessage(TempSensorMock)


_TEMPSENSORMOCK.fields_by_name['value']._options = None
_TEMPSENSORMOCK.fields_by_name['connected']._options = None
_TEMPSENSORMOCK.fields_by_name['strippedFields']._options = None
_TEMPSENSORMOCK._options = None
# @@protoc_insertion_point(module_scope)

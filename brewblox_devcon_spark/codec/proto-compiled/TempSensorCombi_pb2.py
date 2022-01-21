# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TempSensorCombi.proto
"""Generated protocol buffer code."""
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
  name='TempSensorCombi.proto',
  package='blox.TempSensorCombi',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15TempSensorCombi.proto\x12\x14\x62lox.TempSensorCombi\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xd8\x01\n\x0fTempSensorCombi\x12-\n\x05value\x18\x01 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x8a\xb5\x18\x02(\x01\x92?\x02\x38 \x12:\n\x0b\x63ombineFunc\x18\x02 \x01(\x0e\x32%.blox.TempSensorCombi.SensorCombiFunc\x12!\n\x07sensors\x18\x03 \x03(\rB\x10\x8a\xb5\x18\x02\x18\x02\x92?\x02\x38\x10\x92?\x02\x10\x08\x12(\n\x0estrippedFields\x18\x63 \x03(\rB\x10\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x92?\x02\x10\x01:\r\x8a\xb5\x18\x03\x18\xc4\x02\x8a\xb5\x18\x02H\x02*b\n\x0fSensorCombiFunc\x12\x19\n\x15SENSOR_COMBI_FUNC_AVG\x10\x00\x12\x19\n\x15SENSOR_COMBI_FUNC_MIN\x10\x01\x12\x19\n\x15SENSOR_COMBI_FUNC_MAX\x10\x02\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])

_SENSORCOMBIFUNC = _descriptor.EnumDescriptor(
  name='SensorCombiFunc',
  full_name='blox.TempSensorCombi.SensorCombiFunc',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SENSOR_COMBI_FUNC_AVG', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_COMBI_FUNC_MIN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_COMBI_FUNC_MAX', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=296,
  serialized_end=394,
)
_sym_db.RegisterEnumDescriptor(_SENSORCOMBIFUNC)

SensorCombiFunc = enum_type_wrapper.EnumTypeWrapper(_SENSORCOMBIFUNC)
SENSOR_COMBI_FUNC_AVG = 0
SENSOR_COMBI_FUNC_MIN = 1
SENSOR_COMBI_FUNC_MAX = 2



_TEMPSENSORCOMBI = _descriptor.Descriptor(
  name='TempSensorCombi',
  full_name='blox.TempSensorCombi.TempSensorCombi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.TempSensorCombi.TempSensorCombi.value', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \212\265\030\002(\001\222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='combineFunc', full_name='blox.TempSensorCombi.TempSensorCombi.combineFunc', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensors', full_name='blox.TempSensorCombi.TempSensorCombi.sensors', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\002\222?\0028\020\222?\002\020\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strippedFields', full_name='blox.TempSensorCombi.TempSensorCombi.strippedFields', index=3,
      number=99, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\020\222?\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\304\002\212\265\030\002H\002',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=294,
)

_TEMPSENSORCOMBI.fields_by_name['combineFunc'].enum_type = _SENSORCOMBIFUNC
DESCRIPTOR.message_types_by_name['TempSensorCombi'] = _TEMPSENSORCOMBI
DESCRIPTOR.enum_types_by_name['SensorCombiFunc'] = _SENSORCOMBIFUNC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TempSensorCombi = _reflection.GeneratedProtocolMessageType('TempSensorCombi', (_message.Message,), {
  'DESCRIPTOR' : _TEMPSENSORCOMBI,
  '__module__' : 'TempSensorCombi_pb2'
  # @@protoc_insertion_point(class_scope:blox.TempSensorCombi.TempSensorCombi)
  })
_sym_db.RegisterMessage(TempSensorCombi)


_TEMPSENSORCOMBI.fields_by_name['value']._options = None
_TEMPSENSORCOMBI.fields_by_name['sensors']._options = None
_TEMPSENSORCOMBI.fields_by_name['strippedFields']._options = None
_TEMPSENSORCOMBI._options = None
# @@protoc_insertion_point(module_scope)

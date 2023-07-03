# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActuatorAnalogMock.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import Constraints_pb2 as Constraints__pb2
import Claims_pb2 as Claims__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x41\x63tuatorAnalogMock.proto\x12\x17\x62lox.ActuatorAnalogMock\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\x11\x43onstraints.proto\x1a\x0c\x43laims.proto\"\xca\x04\n\x05\x42lock\x12\x0f\n\x07\x65nabled\x18\r \x01(\x08\x12)\n\rstoredSetting\x18\x0b \x01(\x11\x42\x12\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x30\n\x0e\x64\x65siredSetting\x18\t \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12)\n\x07setting\x18\x01 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\'\n\x05value\x18\x02 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12 \n\nminSetting\x18\x04 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12 \n\nmaxSetting\x18\x05 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x1e\n\x08minValue\x18\x06 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x1e\n\x08maxValue\x18\x07 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x44\n\rconstrainedBy\x18\x08 \x01(\x0b\x32-.blox.Constraints.DeprecatedAnalogConstraints\x12\x38\n\x0b\x63onstraints\x18\x0e \x01(\x0b\x32#.blox.Constraints.AnalogConstraints\x12%\n\tclaimedBy\x18\n \x01(\rB\x12\x8a\xb5\x18\x03\x18\xff\x01\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x12-\n\x0bsettingMode\x18\x0c \x01(\x0e\x32\x18.blox.Claims.SettingMode:%\x8a\xb5\x18\x03\x18\xb1\x02\x8a\xb5\x18\x02H\x01\x8a\xb5\x18\x02H\x05\x8a\xb5\x18\x02H\x13\x8a\xb5\x18\x02H\x0f\x8a\xb5\x18\x02H\x10\x62\x06proto3')



_BLOCK = DESCRIPTOR.message_types_by_name['Block']
Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'ActuatorAnalogMock_pb2'
  # @@protoc_insertion_point(class_scope:blox.ActuatorAnalogMock.Block)
  })
_sym_db.RegisterMessage(Block)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BLOCK.fields_by_name['storedSetting']._options = None
  _BLOCK.fields_by_name['storedSetting']._serialized_options = b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 '
  _BLOCK.fields_by_name['desiredSetting']._options = None
  _BLOCK.fields_by_name['desiredSetting']._serialized_options = b'\212\265\030\0020\001\212\265\030\002(\001\212\265\030\003\020\200 \222?\0028 '
  _BLOCK.fields_by_name['setting']._options = None
  _BLOCK.fields_by_name['setting']._serialized_options = b'\212\265\030\0020\001\212\265\030\002(\001\212\265\030\003\020\200 \222?\0028 '
  _BLOCK.fields_by_name['value']._options = None
  _BLOCK.fields_by_name['value']._serialized_options = b'\212\265\030\0020\001\212\265\030\002(\001\212\265\030\003\020\200 \222?\0028 '
  _BLOCK.fields_by_name['minSetting']._options = None
  _BLOCK.fields_by_name['minSetting']._serialized_options = b'\212\265\030\003\020\200 \222?\0028 '
  _BLOCK.fields_by_name['maxSetting']._options = None
  _BLOCK.fields_by_name['maxSetting']._serialized_options = b'\212\265\030\003\020\200 \222?\0028 '
  _BLOCK.fields_by_name['minValue']._options = None
  _BLOCK.fields_by_name['minValue']._serialized_options = b'\212\265\030\003\020\200 \222?\0028 '
  _BLOCK.fields_by_name['maxValue']._options = None
  _BLOCK.fields_by_name['maxValue']._serialized_options = b'\212\265\030\003\020\200 \222?\0028 '
  _BLOCK.fields_by_name['claimedBy']._options = None
  _BLOCK.fields_by_name['claimedBy']._serialized_options = b'\212\265\030\003\030\377\001\212\265\030\002(\001\222?\0028\020'
  _BLOCK._options = None
  _BLOCK._serialized_options = b'\212\265\030\003\030\261\002\212\265\030\002H\001\212\265\030\002H\005\212\265\030\002H\023\212\265\030\002H\017\212\265\030\002H\020'
  _BLOCK._serialized_start=117
  _BLOCK._serialized_end=703
# @@protoc_insertion_point(module_scope)

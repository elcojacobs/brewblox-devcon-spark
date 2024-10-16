# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActuatorAnalogMock.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import Constraints_pb2 as Constraints__pb2
import Claims_pb2 as Claims__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x41\x63tuatorAnalogMock.proto\x12\x17\x62lox.ActuatorAnalogMock\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\x11\x43onstraints.proto\x1a\x0c\x43laims.proto\"\xb0\x04\n\x05\x42lock\x12\x17\n\x07\x65nabled\x18\r \x01(\x08\x42\x06\x8a\xb5\x18\x02x\x01\x12\'\n\rstoredSetting\x18\x0b \x01(\x11\x42\x10\x92?\x02\x38 \x8a\xb5\x18\x07\x10\x80 0\x01x\x01\x12(\n\x0e\x64\x65siredSetting\x18\t \x01(\x11\x42\x10\x92?\x02\x38 \x8a\xb5\x18\x07\x10\x80 (\x01\x30\x01\x12!\n\x07setting\x18\x01 \x01(\x11\x42\x10\x92?\x02\x38 \x8a\xb5\x18\x07\x10\x80 (\x01\x30\x01\x12\x1f\n\x05value\x18\x02 \x01(\x11\x42\x10\x92?\x02\x38 \x8a\xb5\x18\x07\x10\x80 (\x01\x30\x01\x12\"\n\nminSetting\x18\x04 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x10\x80 x\x01\x12\"\n\nmaxSetting\x18\x05 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x10\x80 x\x01\x12 \n\x08minValue\x18\x06 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x10\x80 x\x01\x12 \n\x08maxValue\x18\x07 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x10\x80 x\x01\x12\x44\n\rconstrainedBy\x18\x08 \x01(\x0b\x32-.blox.Constraints.DeprecatedAnalogConstraints\x12@\n\x0b\x63onstraints\x18\x0e \x01(\x0b\x32#.blox.Constraints.AnalogConstraintsB\x06\x8a\xb5\x18\x02x\x01\x12\x1c\n\tclaimedBy\x18\n \x01(\rB\t\x8a\xb5\x18\x05\x18\xff\x01(\x01\x12\x35\n\x0bsettingMode\x18\x0c \x01(\x0e\x32\x18.blox.Claims.SettingModeB\x06\x8a\xb5\x18\x02x\x01:\x0e\x8a\xb5\x18\n\x18\xb1\x02J\x05\x01\x05\x13\x0f\x10\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ActuatorAnalogMock_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BLOCK'].fields_by_name['enabled']._options = None
  _globals['_BLOCK'].fields_by_name['enabled']._serialized_options = b'\212\265\030\002x\001'
  _globals['_BLOCK'].fields_by_name['storedSetting']._options = None
  _globals['_BLOCK'].fields_by_name['storedSetting']._serialized_options = b'\222?\0028 \212\265\030\007\020\200 0\001x\001'
  _globals['_BLOCK'].fields_by_name['desiredSetting']._options = None
  _globals['_BLOCK'].fields_by_name['desiredSetting']._serialized_options = b'\222?\0028 \212\265\030\007\020\200 (\0010\001'
  _globals['_BLOCK'].fields_by_name['setting']._options = None
  _globals['_BLOCK'].fields_by_name['setting']._serialized_options = b'\222?\0028 \212\265\030\007\020\200 (\0010\001'
  _globals['_BLOCK'].fields_by_name['value']._options = None
  _globals['_BLOCK'].fields_by_name['value']._serialized_options = b'\222?\0028 \212\265\030\007\020\200 (\0010\001'
  _globals['_BLOCK'].fields_by_name['minSetting']._options = None
  _globals['_BLOCK'].fields_by_name['minSetting']._serialized_options = b'\222?\0028 \212\265\030\005\020\200 x\001'
  _globals['_BLOCK'].fields_by_name['maxSetting']._options = None
  _globals['_BLOCK'].fields_by_name['maxSetting']._serialized_options = b'\222?\0028 \212\265\030\005\020\200 x\001'
  _globals['_BLOCK'].fields_by_name['minValue']._options = None
  _globals['_BLOCK'].fields_by_name['minValue']._serialized_options = b'\222?\0028 \212\265\030\005\020\200 x\001'
  _globals['_BLOCK'].fields_by_name['maxValue']._options = None
  _globals['_BLOCK'].fields_by_name['maxValue']._serialized_options = b'\222?\0028 \212\265\030\005\020\200 x\001'
  _globals['_BLOCK'].fields_by_name['constraints']._options = None
  _globals['_BLOCK'].fields_by_name['constraints']._serialized_options = b'\212\265\030\002x\001'
  _globals['_BLOCK'].fields_by_name['claimedBy']._options = None
  _globals['_BLOCK'].fields_by_name['claimedBy']._serialized_options = b'\212\265\030\005\030\377\001(\001'
  _globals['_BLOCK'].fields_by_name['settingMode']._options = None
  _globals['_BLOCK'].fields_by_name['settingMode']._serialized_options = b'\212\265\030\002x\001'
  _globals['_BLOCK']._options = None
  _globals['_BLOCK']._serialized_options = b'\212\265\030\n\030\261\002J\005\001\005\023\017\020'
  _globals['_BLOCK']._serialized_start=117
  _globals['_BLOCK']._serialized_end=677
# @@protoc_insertion_point(module_scope)

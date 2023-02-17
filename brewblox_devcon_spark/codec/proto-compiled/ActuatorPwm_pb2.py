# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActuatorPwm.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import Constraints_pb2 as Constraints__pb2
import Claims_pb2 as Claims__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ActuatorPwm.proto',
  package='blox.ActuatorPwm',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x41\x63tuatorPwm.proto\x12\x10\x62lox.ActuatorPwm\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\x11\x43onstraints.proto\x1a\x0c\x43laims.proto\"\xad\x04\n\x05\x42lock\x12\x0f\n\x07\x65nabled\x18\x08 \x01(\x08\x12\x1f\n\nactuatorId\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x06\x92?\x02\x38\x10\x12)\n\rstoredSetting\x18\x0b \x01(\x11\x42\x12\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x30\n\x0e\x64\x65siredSetting\x18\t \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12)\n\x07setting\x18\x04 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\'\n\x05value\x18\x05 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x1d\n\x06period\x18\x03 \x01(\rB\r\x8a\xb5\x18\x02\x08\x03\x8a\xb5\x18\x03\x10\xe8\x07\x12\x44\n\rconstrainedBy\x18\x06 \x01(\x0b\x32-.blox.Constraints.DeprecatedAnalogConstraints\x12\x38\n\x0b\x63onstraints\x18\r \x01(\x0b\x32#.blox.Constraints.AnalogConstraints\x12%\n\tclaimedBy\x18\n \x01(\rB\x12\x8a\xb5\x18\x03\x18\xff\x01\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x12-\n\x0bsettingMode\x18\x0c \x01(\x0e\x32\x18.blox.Claims.SettingMode\x12%\n\x10\x64rivenActuatorId\x18Z \x01(\x08\x42\x0b\x8a\xb5\x18\x02H\x01\x92?\x02\x18\x03:%\x8a\xb5\x18\x03\x18\xb3\x02\x8a\xb5\x18\x02H\x01\x8a\xb5\x18\x02H\x05\x8a\xb5\x18\x02H\x13\x8a\xb5\x18\x02H\x0f\x8a\xb5\x18\x02H\x10\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,Constraints__pb2.DESCRIPTOR,Claims__pb2.DESCRIPTOR,])




_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.ActuatorPwm.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='blox.ActuatorPwm.Block.enabled', index=0,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actuatorId', full_name='blox.ActuatorPwm.Block.actuatorId', index=1,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\006\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storedSetting', full_name='blox.ActuatorPwm.Block.storedSetting', index=2,
      number=11, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desiredSetting', full_name='blox.ActuatorPwm.Block.desiredSetting', index=3,
      number=9, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setting', full_name='blox.ActuatorPwm.Block.setting', index=4,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.ActuatorPwm.Block.value', index=5,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='blox.ActuatorPwm.Block.period', index=6,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\003\212\265\030\003\020\350\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constrainedBy', full_name='blox.ActuatorPwm.Block.constrainedBy', index=7,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='blox.ActuatorPwm.Block.constraints', index=8,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claimedBy', full_name='blox.ActuatorPwm.Block.claimedBy', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\003\030\377\001\212\265\030\002(\001\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settingMode', full_name='blox.ActuatorPwm.Block.settingMode', index=10,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drivenActuatorId', full_name='blox.ActuatorPwm.Block.drivenActuatorId', index=11,
      number=90, type=8, cpp_type=7, label=1,
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
  serialized_options=b'\212\265\030\003\030\263\002\212\265\030\002H\001\212\265\030\002H\005\212\265\030\002H\023\212\265\030\002H\017\212\265\030\002H\020',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=660,
)

_BLOCK.fields_by_name['constrainedBy'].message_type = Constraints__pb2._DEPRECATEDANALOGCONSTRAINTS
_BLOCK.fields_by_name['constraints'].message_type = Constraints__pb2._ANALOGCONSTRAINTS
_BLOCK.fields_by_name['settingMode'].enum_type = Claims__pb2._SETTINGMODE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'ActuatorPwm_pb2'
  # @@protoc_insertion_point(class_scope:blox.ActuatorPwm.Block)
  })
_sym_db.RegisterMessage(Block)


_BLOCK.fields_by_name['actuatorId']._options = None
_BLOCK.fields_by_name['storedSetting']._options = None
_BLOCK.fields_by_name['desiredSetting']._options = None
_BLOCK.fields_by_name['setting']._options = None
_BLOCK.fields_by_name['value']._options = None
_BLOCK.fields_by_name['period']._options = None
_BLOCK.fields_by_name['claimedBy']._options = None
_BLOCK.fields_by_name['drivenActuatorId']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

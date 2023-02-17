# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DigitalActuator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import Constraints_pb2 as Constraints__pb2
import IoArray_pb2 as IoArray__pb2
import Claims_pb2 as Claims__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DigitalActuator.proto',
  package='blox.DigitalActuator',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x44igitalActuator.proto\x12\x14\x62lox.DigitalActuator\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\x11\x43onstraints.proto\x1a\rIoArray.proto\x1a\x0c\x43laims.proto\"\xab\x05\n\x05\x42lock\x12\x1d\n\x08hwDevice\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\n\x92?\x02\x38\x10\x12\x16\n\x07\x63hannel\x18\x02 \x01(\rB\x05\x92?\x02\x38\x08\x12\x37\n\x0bstoredState\x18\x0b \x01(\x0e\x32\x1a.blox.IoArray.DigitalStateB\x06\x8a\xb5\x18\x02\x30\x01\x12>\n\x0c\x64\x65siredState\x18\x06 \x01(\x0e\x32\x1a.blox.IoArray.DigitalStateB\x0c\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x12\x37\n\x05state\x18\x03 \x01(\x0e\x32\x1a.blox.IoArray.DigitalStateB\x0c\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x12\x0e\n\x06invert\x18\x04 \x01(\x08\x12\x45\n\rconstrainedBy\x18\x05 \x01(\x0b\x32..blox.Constraints.DeprecatedDigitalConstraints\x12\x39\n\x0b\x63onstraints\x18\r \x01(\x0b\x32$.blox.Constraints.DigitalConstraints\x12H\n\x18transitionDurationPreset\x18\x07 \x01(\x0e\x32&.blox.IoArray.TransitionDurationPreset\x12\x30\n\x19transitionDurationSetting\x18\x08 \x01(\rB\r\x8a\xb5\x18\x02\x08\x03\x8a\xb5\x18\x03\x10\xe8\x07\x12\x34\n\x17transitionDurationValue\x18\t \x01(\rB\x13\x8a\xb5\x18\x02\x08\x03\x8a\xb5\x18\x03\x10\xe8\x07\x8a\xb5\x18\x02(\x01\x12%\n\tclaimedBy\x18\n \x01(\rB\x12\x8a\xb5\x18\x03\x18\xff\x01\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x12-\n\x0bsettingMode\x18\x0c \x01(\x0e\x32\x18.blox.Claims.SettingMode:\x1f\x8a\xb5\x18\x03\x18\xbe\x02\x8a\xb5\x18\x02H\x06\x8a\xb5\x18\x02H\x15\x8a\xb5\x18\x02H\x10\x8a\xb5\x18\x02H\x11\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,Constraints__pb2.DESCRIPTOR,IoArray__pb2.DESCRIPTOR,Claims__pb2.DESCRIPTOR,])




_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.DigitalActuator.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hwDevice', full_name='blox.DigitalActuator.Block.hwDevice', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\n\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='blox.DigitalActuator.Block.channel', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storedState', full_name='blox.DigitalActuator.Block.storedState', index=2,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desiredState', full_name='blox.DigitalActuator.Block.desiredState', index=3,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='blox.DigitalActuator.Block.state', index=4,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invert', full_name='blox.DigitalActuator.Block.invert', index=5,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constrainedBy', full_name='blox.DigitalActuator.Block.constrainedBy', index=6,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='blox.DigitalActuator.Block.constraints', index=7,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transitionDurationPreset', full_name='blox.DigitalActuator.Block.transitionDurationPreset', index=8,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transitionDurationSetting', full_name='blox.DigitalActuator.Block.transitionDurationSetting', index=9,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\003\212\265\030\003\020\350\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transitionDurationValue', full_name='blox.DigitalActuator.Block.transitionDurationValue', index=10,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\003\212\265\030\003\020\350\007\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claimedBy', full_name='blox.DigitalActuator.Block.claimedBy', index=11,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\003\030\377\001\212\265\030\002(\001\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settingMode', full_name='blox.DigitalActuator.Block.settingMode', index=12,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\276\002\212\265\030\002H\006\212\265\030\002H\025\212\265\030\002H\020\212\265\030\002H\021',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=809,
)

_BLOCK.fields_by_name['storedState'].enum_type = IoArray__pb2._DIGITALSTATE
_BLOCK.fields_by_name['desiredState'].enum_type = IoArray__pb2._DIGITALSTATE
_BLOCK.fields_by_name['state'].enum_type = IoArray__pb2._DIGITALSTATE
_BLOCK.fields_by_name['constrainedBy'].message_type = Constraints__pb2._DEPRECATEDDIGITALCONSTRAINTS
_BLOCK.fields_by_name['constraints'].message_type = Constraints__pb2._DIGITALCONSTRAINTS
_BLOCK.fields_by_name['transitionDurationPreset'].enum_type = IoArray__pb2._TRANSITIONDURATIONPRESET
_BLOCK.fields_by_name['settingMode'].enum_type = Claims__pb2._SETTINGMODE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'DigitalActuator_pb2'
  # @@protoc_insertion_point(class_scope:blox.DigitalActuator.Block)
  })
_sym_db.RegisterMessage(Block)


_BLOCK.fields_by_name['hwDevice']._options = None
_BLOCK.fields_by_name['channel']._options = None
_BLOCK.fields_by_name['storedState']._options = None
_BLOCK.fields_by_name['desiredState']._options = None
_BLOCK.fields_by_name['state']._options = None
_BLOCK.fields_by_name['transitionDurationSetting']._options = None
_BLOCK.fields_by_name['transitionDurationValue']._options = None
_BLOCK.fields_by_name['claimedBy']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

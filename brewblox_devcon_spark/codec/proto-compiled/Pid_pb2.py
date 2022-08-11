# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Pid.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import SetpointSensorPair_pb2 as SetpointSensorPair__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Pid.proto',
  package='blox.Pid',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tPid.proto\x12\x08\x62lox.Pid\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\x18SetpointSensorPair.proto\"\xbe\x07\n\x05\x42lock\x12\x1c\n\x07inputId\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x04\x92?\x02\x38\x10\x12\x1d\n\x08outputId\x18\x02 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x05\x92?\x02\x38\x10\x12\x32\n\ninputValue\x18\x05 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x34\n\x0cinputSetting\x18\x06 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12-\n\x0boutputValue\x18\x07 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12/\n\routputSetting\x18\x08 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x17\n\x07\x65nabled\x18\x0b \x01(\x08\x42\x06\x8a\xb5\x18\x02\x30\x01\x12\x1c\n\x06\x61\x63tive\x18\x0c \x01(\x08\x42\x0c\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x12\x1e\n\x02kp\x18\r \x01(\x11\x42\x12\x8a\xb5\x18\x02\x08\x02\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x17\n\x02ti\x18\x0e \x01(\rB\x0b\x8a\xb5\x18\x02\x08\x03\x92?\x02\x38\x10\x12\x17\n\x02td\x18\x0f \x01(\rB\x0b\x8a\xb5\x18\x02\x08\x03\x92?\x02\x38\x10\x12#\n\x01p\x18\x10 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12#\n\x01i\x18\x11 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12#\n\x01\x64\x18\x12 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12-\n\x05\x65rror\x18\x13 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x06\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x32\n\x08integral\x18\x14 \x01(\x11\x42 \x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x0c\x8a\xb5\x18\x05\x10\x80\x80\x84\x07\x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x33\n\nderivative\x18\x15 \x01(\x11\x42\x1f\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x08\x8a\xb5\x18\x04\x10\xa2\xc4\x08\x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12)\n\rintegralReset\x18\x17 \x01(\x11\x42\x12\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12+\n\x0f\x62oilPointAdjust\x18\x18 \x01(\x11\x42\x12\x8a\xb5\x18\x02\x08\x06\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12#\n\rboilMinOutput\x18\x19 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12$\n\x0e\x62oilModeActive\x18\x1a \x01(\x08\x42\x0c\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x12G\n\x10\x64\x65rivativeFilter\x18\x1b \x01(\x0e\x32%.blox.SetpointSensorPair.FilterChoiceB\x06\x8a\xb5\x18\x02(\x01\x12#\n\x0e\x64rivenOutputId\x18Z \x01(\x08\x42\x0b\x8a\xb5\x18\x02H\x01\x92?\x02\x18\x03:\r\x8a\xb5\x18\x03\x18\xb0\x02\x8a\xb5\x18\x02H\x0f\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,SetpointSensorPair__pb2.DESCRIPTOR,])




_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.Pid.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputId', full_name='blox.Pid.Block.inputId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\004\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputId', full_name='blox.Pid.Block.outputId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\005\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputValue', full_name='blox.Pid.Block.inputValue', index=2,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputSetting', full_name='blox.Pid.Block.inputSetting', index=3,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputValue', full_name='blox.Pid.Block.outputValue', index=4,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputSetting', full_name='blox.Pid.Block.outputSetting', index=5,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='blox.Pid.Block.enabled', index=6,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='blox.Pid.Block.active', index=7,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kp', full_name='blox.Pid.Block.kp', index=8,
      number=13, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\002\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ti', full_name='blox.Pid.Block.ti', index=9,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\003\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='td', full_name='blox.Pid.Block.td', index=10,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\003\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='p', full_name='blox.Pid.Block.p', index=11,
      number=16, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='i', full_name='blox.Pid.Block.i', index=12,
      number=17, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='d', full_name='blox.Pid.Block.d', index=13,
      number=18, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='blox.Pid.Block.error', index=14,
      number=19, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\006\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='integral', full_name='blox.Pid.Block.integral', index=15,
      number=20, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\014\212\265\030\005\020\200\200\204\007\222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='derivative', full_name='blox.Pid.Block.derivative', index=16,
      number=21, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\010\212\265\030\004\020\242\304\010\222?\0028 \212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='integralReset', full_name='blox.Pid.Block.integralReset', index=17,
      number=23, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boilPointAdjust', full_name='blox.Pid.Block.boilPointAdjust', index=18,
      number=24, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\006\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boilMinOutput', full_name='blox.Pid.Block.boilMinOutput', index=19,
      number=25, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boilModeActive', full_name='blox.Pid.Block.boilModeActive', index=20,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='derivativeFilter', full_name='blox.Pid.Block.derivativeFilter', index=21,
      number=27, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drivenOutputId', full_name='blox.Pid.Block.drivenOutputId', index=22,
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
  serialized_options=b'\212\265\030\003\030\260\002\212\265\030\002H\017',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=1038,
)

_BLOCK.fields_by_name['derivativeFilter'].enum_type = SetpointSensorPair__pb2._FILTERCHOICE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'Pid_pb2'
  # @@protoc_insertion_point(class_scope:blox.Pid.Block)
  })
_sym_db.RegisterMessage(Block)


_BLOCK.fields_by_name['inputId']._options = None
_BLOCK.fields_by_name['outputId']._options = None
_BLOCK.fields_by_name['inputValue']._options = None
_BLOCK.fields_by_name['inputSetting']._options = None
_BLOCK.fields_by_name['outputValue']._options = None
_BLOCK.fields_by_name['outputSetting']._options = None
_BLOCK.fields_by_name['enabled']._options = None
_BLOCK.fields_by_name['active']._options = None
_BLOCK.fields_by_name['kp']._options = None
_BLOCK.fields_by_name['ti']._options = None
_BLOCK.fields_by_name['td']._options = None
_BLOCK.fields_by_name['p']._options = None
_BLOCK.fields_by_name['i']._options = None
_BLOCK.fields_by_name['d']._options = None
_BLOCK.fields_by_name['error']._options = None
_BLOCK.fields_by_name['integral']._options = None
_BLOCK.fields_by_name['derivative']._options = None
_BLOCK.fields_by_name['integralReset']._options = None
_BLOCK.fields_by_name['boilPointAdjust']._options = None
_BLOCK.fields_by_name['boilMinOutput']._options = None
_BLOCK.fields_by_name['boilModeActive']._options = None
_BLOCK.fields_by_name['derivativeFilter']._options = None
_BLOCK.fields_by_name['drivenOutputId']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

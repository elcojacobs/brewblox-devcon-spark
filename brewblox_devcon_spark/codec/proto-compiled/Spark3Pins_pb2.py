# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Spark3Pins.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import IoArray_pb2 as IoArray__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Spark3Pins.proto',
  package='blox.Spark3Pins',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10Spark3Pins.proto\x12\x0f\x62lox.Spark3Pins\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\rIoArray.proto\"\x84\x02\n\x05\x42lock\x12\x18\n\x10\x65nableIoSupply5V\x18\x02 \x01(\x08\x12\x19\n\x11\x65nableIoSupply12V\x18\x03 \x01(\x08\x12\x12\n\nsoundAlarm\x18\x05 \x01(\x08\x12$\n\x08voltage5\x18\x06 \x01(\rB\x12\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x8a\xb5\x18\x03\x10\x9a\x03\x12%\n\tvoltage12\x18\x07 \x01(\rB\x12\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x8a\xb5\x18\x03\x10\x95\x01\x12;\n\x08\x63hannels\x18\x08 \x03(\x0b\x32\x17.blox.IoArray.IoChannelB\x10\x92?\x02\x10\x05\x92?\x02x\x01\x8a\xb5\x18\x02(\x01\x12\x19\n\x04pins\x18Z \x01(\x08\x42\x0b\x8a\xb5\x18\x02H\x01\x92?\x02\x18\x03:\r\x8a\xb5\x18\x03\x18\xbf\x02\x8a\xb5\x18\x02H\n*\x92\x01\n\tChannelId\x12\x11\n\rSPARK3_NO_PIN\x10\x00\x12\x14\n\x10SPARK3_CHAN_TOP1\x10\x01\x12\x14\n\x10SPARK3_CHAN_TOP2\x10\x02\x12\x14\n\x10SPARK3_CHAN_TOP3\x10\x03\x12\x17\n\x13SPARK3_CHAN_BOTTOM1\x10\x04\x12\x17\n\x13SPARK3_CHAN_BOTTOM2\x10\x05\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,IoArray__pb2.DESCRIPTOR,])

_CHANNELID = _descriptor.EnumDescriptor(
  name='ChannelId',
  full_name='blox.Spark3Pins.ChannelId',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPARK3_NO_PIN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPARK3_CHAN_TOP1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPARK3_CHAN_TOP2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPARK3_CHAN_TOP3', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPARK3_CHAN_BOTTOM1', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPARK3_CHAN_BOTTOM2', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=346,
  serialized_end=492,
)
_sym_db.RegisterEnumDescriptor(_CHANNELID)

ChannelId = enum_type_wrapper.EnumTypeWrapper(_CHANNELID)
SPARK3_NO_PIN = 0
SPARK3_CHAN_TOP1 = 1
SPARK3_CHAN_TOP2 = 2
SPARK3_CHAN_TOP3 = 3
SPARK3_CHAN_BOTTOM1 = 4
SPARK3_CHAN_BOTTOM2 = 5



_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.Spark3Pins.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enableIoSupply5V', full_name='blox.Spark3Pins.Block.enableIoSupply5V', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enableIoSupply12V', full_name='blox.Spark3Pins.Block.enableIoSupply12V', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='soundAlarm', full_name='blox.Spark3Pins.Block.soundAlarm', index=2,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voltage5', full_name='blox.Spark3Pins.Block.voltage5', index=3,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\020\212\265\030\003\020\232\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voltage12', full_name='blox.Spark3Pins.Block.voltage12', index=4,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\020\212\265\030\003\020\225\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='blox.Spark3Pins.Block.channels', index=5,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002\020\005\222?\002x\001\212\265\030\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pins', full_name='blox.Spark3Pins.Block.pins', index=6,
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
  serialized_options=b'\212\265\030\003\030\277\002\212\265\030\002H\n',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=343,
)

_BLOCK.fields_by_name['channels'].message_type = IoArray__pb2._IOCHANNEL
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.enum_types_by_name['ChannelId'] = _CHANNELID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'Spark3Pins_pb2'
  # @@protoc_insertion_point(class_scope:blox.Spark3Pins.Block)
  })
_sym_db.RegisterMessage(Block)


_BLOCK.fields_by_name['voltage5']._options = None
_BLOCK.fields_by_name['voltage12']._options = None
_BLOCK.fields_by_name['channels']._options = None
_BLOCK.fields_by_name['pins']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

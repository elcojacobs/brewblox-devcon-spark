# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Spark3Pins.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import IoArray_pb2 as IoArray__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10Spark3Pins.proto\x12\x0f\x62lox.Spark3Pins\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\rIoArray.proto\"\x84\x02\n\x05\x42lock\x12\x18\n\x10\x65nableIoSupply5V\x18\x02 \x01(\x08\x12\x19\n\x11\x65nableIoSupply12V\x18\x03 \x01(\x08\x12\x12\n\nsoundAlarm\x18\x05 \x01(\x08\x12$\n\x08voltage5\x18\x06 \x01(\rB\x12\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x8a\xb5\x18\x03\x10\xe8\x07\x12%\n\tvoltage12\x18\x07 \x01(\rB\x12\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x8a\xb5\x18\x03\x10\xe8\x07\x12;\n\x08\x63hannels\x18\x08 \x03(\x0b\x32\x17.blox.IoArray.IoChannelB\x10\x92?\x02\x10\x05\x92?\x02x\x01\x8a\xb5\x18\x02(\x01\x12\x19\n\x04pins\x18Z \x01(\x08\x42\x0b\x8a\xb5\x18\x02H\x01\x92?\x02\x18\x03:\r\x8a\xb5\x18\x03\x18\xbf\x02\x8a\xb5\x18\x02H\n*\x92\x01\n\tChannelId\x12\x11\n\rSPARK3_NO_PIN\x10\x00\x12\x14\n\x10SPARK3_CHAN_TOP1\x10\x01\x12\x14\n\x10SPARK3_CHAN_TOP2\x10\x02\x12\x14\n\x10SPARK3_CHAN_TOP3\x10\x03\x12\x17\n\x13SPARK3_CHAN_BOTTOM1\x10\x04\x12\x17\n\x13SPARK3_CHAN_BOTTOM2\x10\x05\x62\x06proto3')

_CHANNELID = DESCRIPTOR.enum_types_by_name['ChannelId']
ChannelId = enum_type_wrapper.EnumTypeWrapper(_CHANNELID)
SPARK3_NO_PIN = 0
SPARK3_CHAN_TOP1 = 1
SPARK3_CHAN_TOP2 = 2
SPARK3_CHAN_TOP3 = 3
SPARK3_CHAN_BOTTOM1 = 4
SPARK3_CHAN_BOTTOM2 = 5


_BLOCK = DESCRIPTOR.message_types_by_name['Block']
Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'Spark3Pins_pb2'
  # @@protoc_insertion_point(class_scope:blox.Spark3Pins.Block)
  })
_sym_db.RegisterMessage(Block)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BLOCK.fields_by_name['voltage5']._options = None
  _BLOCK.fields_by_name['voltage5']._serialized_options = b'\212\265\030\002(\001\222?\0028\020\212\265\030\003\020\350\007'
  _BLOCK.fields_by_name['voltage12']._options = None
  _BLOCK.fields_by_name['voltage12']._serialized_options = b'\212\265\030\002(\001\222?\0028\020\212\265\030\003\020\350\007'
  _BLOCK.fields_by_name['channels']._options = None
  _BLOCK.fields_by_name['channels']._serialized_options = b'\222?\002\020\005\222?\002x\001\212\265\030\002(\001'
  _BLOCK.fields_by_name['pins']._options = None
  _BLOCK.fields_by_name['pins']._serialized_options = b'\212\265\030\002H\001\222?\002\030\003'
  _BLOCK._options = None
  _BLOCK._serialized_options = b'\212\265\030\003\030\277\002\212\265\030\002H\n'
  _CHANNELID._serialized_start=346
  _CHANNELID._serialized_end=492
  _BLOCK._serialized_start=83
  _BLOCK._serialized_end=343
# @@protoc_insertion_point(module_scope)

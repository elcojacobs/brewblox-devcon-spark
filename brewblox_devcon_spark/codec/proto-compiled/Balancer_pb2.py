# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Balancer.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x42\x61lancer.proto\x12\rblox.Balancer\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\x90\x01\n\x10\x42\x61lancedActuator\x12$\n\x02id\x18\x01 \x01(\rB\x18\x8a\xb5\x18\x03\x18\xff\x01\x8a\xb5\x18\x02\x30\x00\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x12+\n\trequested\x18\x02 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x00\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12)\n\x07granted\x18\x03 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x00\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\"V\n\x05\x42lock\x12>\n\x07\x63lients\x18\x01 \x03(\x0b\x32\x1f.blox.Balancer.BalancedActuatorB\x0c\x8a\xb5\x18\x02\x30\x00\x8a\xb5\x18\x02(\x01:\r\x8a\xb5\x18\x03\x18\xb5\x02\x8a\xb5\x18\x02H\x07\x62\x06proto3')



_BALANCEDACTUATOR = DESCRIPTOR.message_types_by_name['BalancedActuator']
_BLOCK = DESCRIPTOR.message_types_by_name['Block']
BalancedActuator = _reflection.GeneratedProtocolMessageType('BalancedActuator', (_message.Message,), {
  'DESCRIPTOR' : _BALANCEDACTUATOR,
  '__module__' : 'Balancer_pb2'
  # @@protoc_insertion_point(class_scope:blox.Balancer.BalancedActuator)
  })
_sym_db.RegisterMessage(BalancedActuator)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'Balancer_pb2'
  # @@protoc_insertion_point(class_scope:blox.Balancer.Block)
  })
_sym_db.RegisterMessage(Block)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BALANCEDACTUATOR.fields_by_name['id']._options = None
  _BALANCEDACTUATOR.fields_by_name['id']._serialized_options = b'\212\265\030\003\030\377\001\212\265\030\0020\000\212\265\030\002(\001\222?\0028\020'
  _BALANCEDACTUATOR.fields_by_name['requested']._options = None
  _BALANCEDACTUATOR.fields_by_name['requested']._serialized_options = b'\212\265\030\0020\000\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'
  _BALANCEDACTUATOR.fields_by_name['granted']._options = None
  _BALANCEDACTUATOR.fields_by_name['granted']._serialized_options = b'\212\265\030\0020\000\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'
  _BLOCK.fields_by_name['clients']._options = None
  _BLOCK.fields_by_name['clients']._serialized_options = b'\212\265\030\0020\000\212\265\030\002(\001'
  _BLOCK._options = None
  _BLOCK._serialized_options = b'\212\265\030\003\030\265\002\212\265\030\002H\007'
  _BALANCEDACTUATOR._serialized_start=64
  _BALANCEDACTUATOR._serialized_end=208
  _BLOCK._serialized_start=210
  _BLOCK._serialized_end=296
# @@protoc_insertion_point(module_scope)

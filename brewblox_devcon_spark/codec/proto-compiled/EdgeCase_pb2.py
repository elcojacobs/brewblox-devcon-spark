# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EdgeCase.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x45\x64geCase.proto\x12\rblox.EdgeCase\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"B\n\x08Settings\x12\x17\n\x07\x61\x64\x64ress\x18\x01 \x01(\x06\x42\x06\x8a\xb5\x18\x02 \x01\x12\x1d\n\x06offset\x18\x02 \x01(\x11\x42\r\x8a\xb5\x18\x02\x08\x06\x8a\xb5\x18\x03\x10\x80\x02\"@\n\x05State\x12\x1c\n\x05value\x18\x01 \x01(\x11\x42\r\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80\x02\x12\x19\n\tconnected\x18\x02 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\"(\n\nNestedLink\x12\x1a\n\nconnection\x18\x01 \x01(\rB\x06\x8a\xb5\x18\x02\x18\x02\"\xa6\x02\n\x05\x42lock\x12)\n\x08settings\x18\x01 \x01(\x0b\x32\x17.blox.EdgeCase.Settings\x12#\n\x05state\x18\x02 \x01(\x0b\x32\x14.blox.EdgeCase.State\x12\x14\n\x04link\x18\x03 \x01(\rB\x06\x8a\xb5\x18\x02\x18\x05\x12\x32\n\x0f\x61\x64\x64itionalLinks\x18\x04 \x03(\x0b\x32\x19.blox.EdgeCase.NestedLink\x12!\n\nlistValues\x18\x05 \x03(\x02\x42\r\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80\x02\x12\x1d\n\x06\x64\x65ltaV\x18\x06 \x01(\rB\r\x8a\xb5\x18\x02\x08\x07\x8a\xb5\x18\x03\x10\x80\x02\x12\x16\n\x06logged\x18\x07 \x01(\rB\x06\x8a\xb5\x18\x02\x30\x01\x12\x10\n\x08unLogged\x18\x08 \x01(\r\x12\x17\n\x02ip\x18\n \x01(\rB\x0b\x8a\xb5\x18\x02`\x01\x92?\x02\x38 \"#\n\x07SubCase\x12\x10\n\x08subvalue\x18\x01 \x01(\r:\x06\x8a\xb5\x18\x02X\x01\x62\x06proto3')



_SETTINGS = DESCRIPTOR.message_types_by_name['Settings']
_STATE = DESCRIPTOR.message_types_by_name['State']
_NESTEDLINK = DESCRIPTOR.message_types_by_name['NestedLink']
_BLOCK = DESCRIPTOR.message_types_by_name['Block']
_SUBCASE = DESCRIPTOR.message_types_by_name['SubCase']
Settings = _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), {
  'DESCRIPTOR' : _SETTINGS,
  '__module__' : 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.Settings)
  })
_sym_db.RegisterMessage(Settings)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
  'DESCRIPTOR' : _STATE,
  '__module__' : 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.State)
  })
_sym_db.RegisterMessage(State)

NestedLink = _reflection.GeneratedProtocolMessageType('NestedLink', (_message.Message,), {
  'DESCRIPTOR' : _NESTEDLINK,
  '__module__' : 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.NestedLink)
  })
_sym_db.RegisterMessage(NestedLink)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.Block)
  })
_sym_db.RegisterMessage(Block)

SubCase = _reflection.GeneratedProtocolMessageType('SubCase', (_message.Message,), {
  'DESCRIPTOR' : _SUBCASE,
  '__module__' : 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.SubCase)
  })
_sym_db.RegisterMessage(SubCase)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SETTINGS.fields_by_name['address']._options = None
  _SETTINGS.fields_by_name['address']._serialized_options = b'\212\265\030\002 \001'
  _SETTINGS.fields_by_name['offset']._options = None
  _SETTINGS.fields_by_name['offset']._serialized_options = b'\212\265\030\002\010\006\212\265\030\003\020\200\002'
  _STATE.fields_by_name['value']._options = None
  _STATE.fields_by_name['value']._serialized_options = b'\212\265\030\002\010\001\212\265\030\003\020\200\002'
  _STATE.fields_by_name['connected']._options = None
  _STATE.fields_by_name['connected']._serialized_options = b'\212\265\030\002(\001'
  _NESTEDLINK.fields_by_name['connection']._options = None
  _NESTEDLINK.fields_by_name['connection']._serialized_options = b'\212\265\030\002\030\002'
  _BLOCK.fields_by_name['link']._options = None
  _BLOCK.fields_by_name['link']._serialized_options = b'\212\265\030\002\030\005'
  _BLOCK.fields_by_name['listValues']._options = None
  _BLOCK.fields_by_name['listValues']._serialized_options = b'\212\265\030\002\010\001\212\265\030\003\020\200\002'
  _BLOCK.fields_by_name['deltaV']._options = None
  _BLOCK.fields_by_name['deltaV']._serialized_options = b'\212\265\030\002\010\007\212\265\030\003\020\200\002'
  _BLOCK.fields_by_name['logged']._options = None
  _BLOCK.fields_by_name['logged']._serialized_options = b'\212\265\030\0020\001'
  _BLOCK.fields_by_name['ip']._options = None
  _BLOCK.fields_by_name['ip']._serialized_options = b'\212\265\030\002`\001\222?\0028 '
  _SUBCASE._options = None
  _SUBCASE._serialized_options = b'\212\265\030\002X\001'
  _SETTINGS._serialized_start=63
  _SETTINGS._serialized_end=129
  _STATE._serialized_start=131
  _STATE._serialized_end=195
  _NESTEDLINK._serialized_start=197
  _NESTEDLINK._serialized_end=237
  _BLOCK._serialized_start=240
  _BLOCK._serialized_end=534
  _SUBCASE._serialized_start=536
  _SUBCASE._serialized_end=571
# @@protoc_insertion_point(module_scope)

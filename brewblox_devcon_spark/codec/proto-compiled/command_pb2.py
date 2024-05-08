# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcommand.proto\x12\x07\x63ommand\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"%\n\tMaskField\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x03(\rB\x07\x92?\x04\x10\x04\x38\x10\"\xae\x01\n\x07Payload\x12\x0f\n\x07\x62lockId\x18\x01 \x01(\r\x12&\n\tblockType\x18\x02 \x01(\x0e\x32\x13.brewblox.BlockType\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12#\n\x08maskMode\x18\x06 \x01(\x0e\x32\x11.command.MaskMode\x12&\n\nmaskFields\x18\x07 \x03(\x0b\x32\x12.command.MaskField\"}\n\x07Request\x12\r\n\x05msgId\x18\x01 \x01(\x05\x12\x1f\n\x06opcode\x18\x02 \x01(\x0e\x32\x0f.command.Opcode\x12!\n\x07payload\x18\x03 \x01(\x0b\x32\x10.command.Payload\x12\x1f\n\x04mode\x18\x04 \x01(\x0e\x32\x11.command.ReadMode\"\x80\x01\n\x08Response\x12\r\n\x05msgId\x18\x01 \x01(\x05\x12!\n\x05\x65rror\x18\x02 \x01(\x0e\x32\x12.command.ErrorCode\x12!\n\x07payload\x18\x03 \x03(\x0b\x32\x10.command.Payload\x12\x1f\n\x04mode\x18\x04 \x01(\x0e\x32\x11.command.ReadMode*\xbc\x02\n\x06Opcode\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07VERSION\x10\x01\x12\x0e\n\nBLOCK_READ\x10\n\x12\x12\n\x0e\x42LOCK_READ_ALL\x10\x0b\x12\x0f\n\x0b\x42LOCK_WRITE\x10\x0c\x12\x10\n\x0c\x42LOCK_CREATE\x10\r\x12\x10\n\x0c\x42LOCK_DELETE\x10\x0e\x12\x12\n\x0e\x42LOCK_DISCOVER\x10\x0f\x12\x10\n\x0cSTORAGE_READ\x10\x14\x12\x14\n\x10STORAGE_READ_ALL\x10\x15\x12\r\n\tNAME_READ\x10\x32\x12\x11\n\rNAME_READ_ALL\x10\x33\x12\x0e\n\nNAME_WRITE\x10\x34\x12\n\n\x06REBOOT\x10\x1e\x12\x10\n\x0c\x43LEAR_BLOCKS\x10\x1f\x12\x0e\n\nCLEAR_WIFI\x10 \x12\x11\n\rFACTORY_RESET\x10!\x12\x13\n\x0f\x46IRMWARE_UPDATE\x10(*\xba\x06\n\tErrorCode\x12\x06\n\x02OK\x10\x00\x12\x11\n\rUNKNOWN_ERROR\x10\x01\x12\x12\n\x0eINVALID_OPCODE\x10\x02\x12\x15\n\x11INSUFFICIENT_HEAP\x10\x04\x12\x18\n\x14INSUFFICIENT_STORAGE\x10\x05\x12\x11\n\rNETWORK_ERROR\x10\n\x12\x16\n\x12NETWORK_READ_ERROR\x10\x0b\x12\x1a\n\x16NETWORK_DECODING_ERROR\x10\x0c\x12\x17\n\x13NETWORK_WRITE_ERROR\x10\r\x12\x1a\n\x16NETWORK_ENCODING_ERROR\x10\x0e\x12\x11\n\rSTORAGE_ERROR\x10\x14\x12\x16\n\x12STORAGE_READ_ERROR\x10\x15\x12\x1a\n\x16STORAGE_DECODING_ERROR\x10\x16\x12\x15\n\x11STORAGE_CRC_ERROR\x10\x17\x12\x17\n\x13STORAGE_WRITE_ERROR\x10\x18\x12\x1a\n\x16STORAGE_ENCODING_ERROR\x10\x19\x12\x1f\n\x1bSTORAGE_OUT_OF_BOUNDS_ERROR\x10\x1a\x12\x16\n\x12\x42LOCK_NOT_WRITABLE\x10\x1e\x12\x16\n\x12\x42LOCK_NOT_READABLE\x10\x1f\x12\x17\n\x13\x42LOCK_NOT_CREATABLE\x10 \x12\x17\n\x13\x42LOCK_NOT_DELETABLE\x10!\x12\x11\n\rINVALID_BLOCK\x10(\x12\x14\n\x10INVALID_BLOCK_ID\x10)\x12\x16\n\x12INVALID_BLOCK_TYPE\x10*\x12\x19\n\x15INVALID_BLOCK_CONTENT\x10,\x12\x16\n\x12INVALID_BLOCK_NAME\x10-\x12\x18\n\x14INVALID_STORED_BLOCK\x10\x32\x12\x1b\n\x17INVALID_STORED_BLOCK_ID\x10\x33\x12\x1d\n\x19INVALID_STORED_BLOCK_TYPE\x10\x34\x12 \n\x1cINVALID_STORED_BLOCK_CONTENT\x10\x36\x12\x1d\n\x19INVALID_STORED_BLOCK_NAME\x10\x37\x12\x16\n\x12\x44UPLICATE_BLOCK_ID\x10<\x12\x18\n\x14\x44UPLICATE_BLOCK_NAME\x10=*5\n\x08MaskMode\x12\x0b\n\x07NO_MASK\x10\x00\x12\r\n\tINCLUSIVE\x10\x01\x12\r\n\tEXCLUSIVE\x10\x02*/\n\x08ReadMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\n\n\x06STORED\x10\x01\x12\n\n\x06LOGGED\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'command_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _MASKFIELD.fields_by_name['address']._options = None
  _MASKFIELD.fields_by_name['address']._serialized_options = b'\222?\004\020\0048\020'
  _globals['_OPCODE']._serialized_start=531
  _globals['_OPCODE']._serialized_end=847
  _globals['_ERRORCODE']._serialized_start=850
  _globals['_ERRORCODE']._serialized_end=1676
  _globals['_MASKMODE']._serialized_start=1678
  _globals['_MASKMODE']._serialized_end=1731
  _globals['_READMODE']._serialized_start=1733
  _globals['_READMODE']._serialized_end=1780
  _globals['_MASKFIELD']._serialized_start=56
  _globals['_MASKFIELD']._serialized_end=93
  _globals['_PAYLOAD']._serialized_start=96
  _globals['_PAYLOAD']._serialized_end=270
  _globals['_REQUEST']._serialized_start=272
  _globals['_REQUEST']._serialized_end=397
  _globals['_RESPONSE']._serialized_start=400
  _globals['_RESPONSE']._serialized_end=528
# @@protoc_insertion_point(module_scope)

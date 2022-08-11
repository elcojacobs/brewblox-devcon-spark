# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WiFiSettings.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WiFiSettings.proto',
  package='blox.WiFiSettings',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12WiFiSettings.proto\x12\x11\x62lox.WiFiSettings\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xbb\x01\n\x05\x42lock\x12\x13\n\x04ssid\x18\x01 \x01(\tB\x05\x92?\x02\x08!\x12\x17\n\x08password\x18\x02 \x01(\tB\x05\x92?\x02\x08@\x12-\n\x08security\x18\x03 \x01(\x0e\x32\x1b.blox.WiFiSettings.Security\x12)\n\x06\x63ipher\x18\x04 \x01(\x0e\x32\x19.blox.WiFiSettings.Cipher\x12!\n\x06signal\x18\x05 \x01(\x05\x42\x11\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x02\x30\x01\x92?\x02\x38\x08:\x07\x8a\xb5\x18\x03\x18\xb8\x02*\xa7\x01\n\x08Security\x12\x12\n\x0eWLAN_SEC_UNSEC\x10\x00\x12\x10\n\x0cWLAN_SEC_WEP\x10\x01\x12\x10\n\x0cWLAN_SEC_WPA\x10\x02\x12\x11\n\rWLAN_SEC_WPA2\x10\x03\x12\x1b\n\x17WLAN_SEC_WPA_ENTERPRISE\x10\x04\x12\x1c\n\x18WLAN_SEC_WPA2_ENTERPRISE\x10\x05\x12\x15\n\x10WLAN_SEC_NOT_SET\x10\xff\x01*i\n\x06\x43ipher\x12\x17\n\x13WLAN_CIPHER_NOT_SET\x10\x00\x12\x13\n\x0fWLAN_CIPHER_AES\x10\x01\x12\x14\n\x10WLAN_CIPHER_TKIP\x10\x02\x12\x1b\n\x17WLAN_CIPHER_AES_OR_TKIP\x10\x03\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])

_SECURITY = _descriptor.EnumDescriptor(
  name='Security',
  full_name='blox.WiFiSettings.Security',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WLAN_SEC_UNSEC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WLAN_SEC_WEP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WLAN_SEC_WPA', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WLAN_SEC_WPA2', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WLAN_SEC_WPA_ENTERPRISE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WLAN_SEC_WPA2_ENTERPRISE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WLAN_SEC_NOT_SET', index=6, number=255,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=262,
  serialized_end=429,
)
_sym_db.RegisterEnumDescriptor(_SECURITY)

Security = enum_type_wrapper.EnumTypeWrapper(_SECURITY)
_CIPHER = _descriptor.EnumDescriptor(
  name='Cipher',
  full_name='blox.WiFiSettings.Cipher',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WLAN_CIPHER_NOT_SET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WLAN_CIPHER_AES', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WLAN_CIPHER_TKIP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WLAN_CIPHER_AES_OR_TKIP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=431,
  serialized_end=536,
)
_sym_db.RegisterEnumDescriptor(_CIPHER)

Cipher = enum_type_wrapper.EnumTypeWrapper(_CIPHER)
WLAN_SEC_UNSEC = 0
WLAN_SEC_WEP = 1
WLAN_SEC_WPA = 2
WLAN_SEC_WPA2 = 3
WLAN_SEC_WPA_ENTERPRISE = 4
WLAN_SEC_WPA2_ENTERPRISE = 5
WLAN_SEC_NOT_SET = 255
WLAN_CIPHER_NOT_SET = 0
WLAN_CIPHER_AES = 1
WLAN_CIPHER_TKIP = 2
WLAN_CIPHER_AES_OR_TKIP = 3



_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.WiFiSettings.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ssid', full_name='blox.WiFiSettings.Block.ssid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002\010!', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='blox.WiFiSettings.Block.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002\010@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security', full_name='blox.WiFiSettings.Block.security', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cipher', full_name='blox.WiFiSettings.Block.cipher', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signal', full_name='blox.WiFiSettings.Block.signal', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\212\265\030\0020\001\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\270\002',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=259,
)

_BLOCK.fields_by_name['security'].enum_type = _SECURITY
_BLOCK.fields_by_name['cipher'].enum_type = _CIPHER
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.enum_types_by_name['Security'] = _SECURITY
DESCRIPTOR.enum_types_by_name['Cipher'] = _CIPHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'WiFiSettings_pb2'
  # @@protoc_insertion_point(class_scope:blox.WiFiSettings.Block)
  })
_sym_db.RegisterMessage(Block)


_BLOCK.fields_by_name['ssid']._options = None
_BLOCK.fields_by_name['password']._options = None
_BLOCK.fields_by_name['signal']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

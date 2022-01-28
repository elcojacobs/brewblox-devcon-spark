# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TouchSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
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
  name='TouchSettings.proto',
  package='blox.TouchSettings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13TouchSettings.proto\x12\x12\x62lox.TouchSettings\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xb6\x01\n\x05\x42lock\x12\x32\n\ncalibrated\x18\x01 \x01(\x0e\x32\x1e.blox.TouchSettings.Calibrated\x12\x16\n\x07xOffset\x18\x02 \x01(\x05\x42\x05\x92?\x02\x38\x10\x12\x16\n\x07yOffset\x18\x03 \x01(\x05\x42\x05\x92?\x02\x38\x10\x12\x1f\n\x10xBitsPerPixelX16\x18\x04 \x01(\rB\x05\x92?\x02\x38\x10\x12\x1f\n\x10yBitsPerPixelX16\x18\x05 \x01(\rB\x05\x92?\x02\x38\x10:\x07\x8a\xb5\x18\x03\x18\xb9\x02*G\n\nCalibrated\x12\x11\n\rCALIBRATED_NO\x10\x00\x12\x12\n\x0e\x43\x41LIBRATED_YES\x10\x01\x12\x12\n\x0e\x43\x41LIBRATED_NEW\x10\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])

_CALIBRATED = _descriptor.EnumDescriptor(
  name='Calibrated',
  full_name='blox.TouchSettings.Calibrated',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CALIBRATED_NO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATED_YES', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATED_NEW', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=258,
  serialized_end=329,
)
_sym_db.RegisterEnumDescriptor(_CALIBRATED)

Calibrated = enum_type_wrapper.EnumTypeWrapper(_CALIBRATED)
CALIBRATED_NO = 0
CALIBRATED_YES = 1
CALIBRATED_NEW = 2



_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.TouchSettings.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='calibrated', full_name='blox.TouchSettings.Block.calibrated', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xOffset', full_name='blox.TouchSettings.Block.xOffset', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yOffset', full_name='blox.TouchSettings.Block.yOffset', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xBitsPerPixelX16', full_name='blox.TouchSettings.Block.xBitsPerPixelX16', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yBitsPerPixelX16', full_name='blox.TouchSettings.Block.yBitsPerPixelX16', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\0028\020'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\212\265\030\003\030\271\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=256,
)

_BLOCK.fields_by_name['calibrated'].enum_type = _CALIBRATED
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.enum_types_by_name['Calibrated'] = _CALIBRATED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'TouchSettings_pb2'
  # @@protoc_insertion_point(class_scope:blox.TouchSettings.Block)
  ))
_sym_db.RegisterMessage(Block)


_BLOCK.fields_by_name['xOffset']._options = None
_BLOCK.fields_by_name['yOffset']._options = None
_BLOCK.fields_by_name['xBitsPerPixelX16']._options = None
_BLOCK.fields_by_name['yBitsPerPixelX16']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

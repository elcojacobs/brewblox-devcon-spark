# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EdgeCase.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='EdgeCase.proto',
  package='blox.EdgeCase',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x45\x64geCase.proto\x12\rblox.EdgeCase\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"B\n\x08Settings\x12\x17\n\x07\x61\x64\x64ress\x18\x01 \x01(\x06\x42\x06\x8a\xb5\x18\x02 \x01\x12\x1d\n\x06offset\x18\x02 \x01(\x11\x42\r\x8a\xb5\x18\x02\x08\x06\x8a\xb5\x18\x03\x10\x80\x02\"@\n\x05State\x12\x1c\n\x05value\x18\x01 \x01(\x11\x42\r\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80\x02\x12\x19\n\tconnected\x18\x02 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\"(\n\nNestedLink\x12\x1a\n\nconnection\x18\x01 \x01(\rB\x06\x8a\xb5\x18\x02\x18\x02\"\xe1\x02\n\x05\x42lock\x12)\n\x08settings\x18\x01 \x01(\x0b\x32\x17.blox.EdgeCase.Settings\x12#\n\x05state\x18\x02 \x01(\x0b\x32\x14.blox.EdgeCase.State\x12\x14\n\x04link\x18\x03 \x01(\rB\x06\x8a\xb5\x18\x02\x18\x05\x12\x32\n\x0f\x61\x64\x64itionalLinks\x18\x04 \x03(\x0b\x32\x19.blox.EdgeCase.NestedLink\x12!\n\nlistValues\x18\x05 \x03(\x02\x42\r\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80\x02\x12\x1d\n\x06\x64\x65ltaV\x18\x06 \x01(\rB\r\x8a\xb5\x18\x02\x08\x07\x8a\xb5\x18\x03\x10\x80\x02\x12\x16\n\x06logged\x18\x07 \x01(\rB\x06\x8a\xb5\x18\x02\x30\x01\x12\x10\n\x08unLogged\x18\x08 \x01(\r\x12(\n\x0c\x64rivenDevice\x18\t \x01(\rB\x12\x8a\xb5\x18\x03\x18\xbb\x02\x8a\xb5\x18\x02@\x01\x92?\x02\x38\x10\x12(\n\x0estrippedFields\x18\x63 \x03(\rB\x10\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x92?\x02\x10\x02\"#\n\x07SubCase\x12\x10\n\x08subvalue\x18\x01 \x01(\r:\x06\x8a\xb5\x18\x02X\x01\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_SETTINGS = _descriptor.Descriptor(
  name='Settings',
  full_name='blox.EdgeCase.Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='blox.EdgeCase.Settings.address', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002 \001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='blox.EdgeCase.Settings.offset', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\010\006\212\265\030\003\020\200\002'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=129,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='blox.EdgeCase.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.EdgeCase.State.value', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\010\001\212\265\030\003\020\200\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connected', full_name='blox.EdgeCase.State.connected', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=195,
)


_NESTEDLINK = _descriptor.Descriptor(
  name='NestedLink',
  full_name='blox.EdgeCase.NestedLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection', full_name='blox.EdgeCase.NestedLink.connection', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\002'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=237,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.EdgeCase.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='blox.EdgeCase.Block.settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='blox.EdgeCase.Block.state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='blox.EdgeCase.Block.link', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additionalLinks', full_name='blox.EdgeCase.Block.additionalLinks', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='listValues', full_name='blox.EdgeCase.Block.listValues', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\010\001\212\265\030\003\020\200\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deltaV', full_name='blox.EdgeCase.Block.deltaV', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\010\007\212\265\030\003\020\200\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logged', full_name='blox.EdgeCase.Block.logged', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\0020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unLogged', full_name='blox.EdgeCase.Block.unLogged', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drivenDevice', full_name='blox.EdgeCase.Block.drivenDevice', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\030\273\002\212\265\030\002@\001\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strippedFields', full_name='blox.EdgeCase.Block.strippedFields', index=9,
      number=99, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001\222?\0028\020\222?\002\020\002'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=593,
)


_SUBCASE = _descriptor.Descriptor(
  name='SubCase',
  full_name='blox.EdgeCase.SubCase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subvalue', full_name='blox.EdgeCase.SubCase.subvalue', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\212\265\030\002X\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=595,
  serialized_end=630,
)

_BLOCK.fields_by_name['settings'].message_type = _SETTINGS
_BLOCK.fields_by_name['state'].message_type = _STATE
_BLOCK.fields_by_name['additionalLinks'].message_type = _NESTEDLINK
DESCRIPTOR.message_types_by_name['Settings'] = _SETTINGS
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['NestedLink'] = _NESTEDLINK
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['SubCase'] = _SUBCASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Settings = _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), dict(
  DESCRIPTOR = _SETTINGS,
  __module__ = 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.Settings)
  ))
_sym_db.RegisterMessage(Settings)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.State)
  ))
_sym_db.RegisterMessage(State)

NestedLink = _reflection.GeneratedProtocolMessageType('NestedLink', (_message.Message,), dict(
  DESCRIPTOR = _NESTEDLINK,
  __module__ = 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.NestedLink)
  ))
_sym_db.RegisterMessage(NestedLink)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.Block)
  ))
_sym_db.RegisterMessage(Block)

SubCase = _reflection.GeneratedProtocolMessageType('SubCase', (_message.Message,), dict(
  DESCRIPTOR = _SUBCASE,
  __module__ = 'EdgeCase_pb2'
  # @@protoc_insertion_point(class_scope:blox.EdgeCase.SubCase)
  ))
_sym_db.RegisterMessage(SubCase)


_SETTINGS.fields_by_name['address']._options = None
_SETTINGS.fields_by_name['offset']._options = None
_STATE.fields_by_name['value']._options = None
_STATE.fields_by_name['connected']._options = None
_NESTEDLINK.fields_by_name['connection']._options = None
_BLOCK.fields_by_name['link']._options = None
_BLOCK.fields_by_name['listValues']._options = None
_BLOCK.fields_by_name['deltaV']._options = None
_BLOCK.fields_by_name['logged']._options = None
_BLOCK.fields_by_name['drivenDevice']._options = None
_BLOCK.fields_by_name['strippedFields']._options = None
_SUBCASE._options = None
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Constraints.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x43onstraints.proto\x12\x10\x62lox.Constraints\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"c\n\x0fValueConstraint\x12\x1d\n\x05value\x18\x01 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x10\x80 x\x01\x12\x17\n\x07\x65nabled\x18\x32 \x01(\x08\x42\x06\x8a\xb5\x18\x02x\x01\x12\x18\n\x08limiting\x18\x33 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\"\x9a\x01\n\x12\x42\x61lancedConstraint\x12\x1c\n\nbalancerId\x18\x01 \x01(\rB\x08\x8a\xb5\x18\x04\x18\x07x\x01\x12\x1a\n\x07granted\x18\x02 \x01(\rB\t\x8a\xb5\x18\x05\x10\x80 (\x01\x12\x17\n\x07\x65nabled\x18\x32 \x01(\x08\x42\x06\x8a\xb5\x18\x02x\x01\x12\x18\n\x08limiting\x18\x33 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12\x17\n\x02id\x18Z \x01(\x08\x42\x0b\x92?\x02\x18\x03\x8a\xb5\x18\x02H\x01\"\x90\x01\n\x12\x44urationConstraint\x12\"\n\x08\x64uration\x18\x01 \x01(\rB\x10\x92?\x02\x38 \x8a\xb5\x18\x07\x08\x03\x10\xe8\x07x\x01\x12\x17\n\x07\x65nabled\x18\x32 \x01(\x08\x42\x06\x8a\xb5\x18\x02x\x01\x12\x18\n\x08limiting\x18\x33 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12#\n\tremaining\x18\x34 \x01(\rB\x10\x92?\x02\x38 \x8a\xb5\x18\x07\x08\x03\x10\xe8\x07(\x01\"\xf0\x01\n\x11MutexedConstraint\x12\x19\n\x07mutexId\x18\x01 \x01(\rB\x08\x8a\xb5\x18\x04\x18\x08x\x01\x12\'\n\rextraHoldTime\x18\x02 \x01(\rB\x10\x92?\x02\x38 \x8a\xb5\x18\x07\x08\x03\x10\xe8\x07x\x01\x12\x17\n\x07hasLock\x18\x04 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12\x17\n\x07\x65nabled\x18\x32 \x01(\x08\x42\x06\x8a\xb5\x18\x02x\x01\x12\x18\n\x08limiting\x18\x33 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12#\n\tremaining\x18\x34 \x01(\rB\x10\x92?\x02\x38 \x8a\xb5\x18\x07\x08\x03\x10\xe8\x07(\x01\x12&\n\x11hasCustomHoldTime\x18Z \x01(\x08\x42\x0b\x92?\x02\x18\x03\x8a\xb5\x18\x02H\x01\"\xc3\x01\n\x11\x41nalogConstraints\x12\x36\n\x03min\x18\x01 \x01(\x0b\x32!.blox.Constraints.ValueConstraintB\x06\x8a\xb5\x18\x02x\x01\x12\x36\n\x03max\x18\x02 \x01(\x0b\x32!.blox.Constraints.ValueConstraintB\x06\x8a\xb5\x18\x02x\x01\x12>\n\x08\x62\x61lanced\x18\x03 \x01(\x0b\x32$.blox.Constraints.BalancedConstraintB\x06\x8a\xb5\x18\x02x\x01\"\xd0\x02\n\x12\x44igitalConstraints\x12<\n\x06minOff\x18\x01 \x01(\x0b\x32$.blox.Constraints.DurationConstraintB\x06\x8a\xb5\x18\x02x\x01\x12;\n\x05minOn\x18\x02 \x01(\x0b\x32$.blox.Constraints.DurationConstraintB\x06\x8a\xb5\x18\x02x\x01\x12@\n\ndelayedOff\x18\x03 \x01(\x0b\x32$.blox.Constraints.DurationConstraintB\x06\x8a\xb5\x18\x02x\x01\x12?\n\tdelayedOn\x18\x04 \x01(\x0b\x32$.blox.Constraints.DurationConstraintB\x06\x8a\xb5\x18\x02x\x01\x12<\n\x07mutexed\x18\x05 \x01(\x0b\x32#.blox.Constraints.MutexedConstraintB\x06\x8a\xb5\x18\x02x\x01\"\xb8\x01\n\x1a\x44\x65precatedAnalogConstraint\x12\x1b\n\x03min\x18\x01 \x01(\x11\x42\x0c\x92?\x02\x38 \x8a\xb5\x18\x03\x10\x80 H\x00\x12\x1b\n\x03max\x18\x02 \x01(\x11\x42\x0c\x92?\x02\x38 \x8a\xb5\x18\x03\x10\x80 H\x00\x12\x38\n\x08\x62\x61lanced\x18\x03 \x01(\x0b\x32$.blox.Constraints.BalancedConstraintH\x00\x12\x18\n\x08limiting\x18\x64 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x42\x0c\n\nconstraint\"g\n\x1b\x44\x65precatedAnalogConstraints\x12H\n\x0b\x63onstraints\x18\x01 \x03(\x0b\x32,.blox.Constraints.DeprecatedAnalogConstraintB\x05\x92?\x02\x10\x08\"\xce\x02\n\x1b\x44\x65precatedDigitalConstraint\x12 \n\x06minOff\x18\x01 \x01(\rB\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x08\x03\x10\xe8\x07H\x00\x12\x1f\n\x05minOn\x18\x02 \x01(\rB\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x08\x03\x10\xe8\x07H\x00\x12\x36\n\x07mutexed\x18\x04 \x01(\x0b\x32#.blox.Constraints.MutexedConstraintH\x00\x12$\n\ndelayedOff\x18\x05 \x01(\rB\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x08\x03\x10\xe8\x07H\x00\x12#\n\tdelayedOn\x18\x06 \x01(\rB\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x08\x03\x10\xe8\x07H\x00\x12\x17\n\x05mutex\x18\x03 \x01(\rB\x06\x8a\xb5\x18\x02\x18\x08H\x00\x12\x1d\n\x08limiting\x18\x64 \x01(\rB\x0b\x92?\x02\x18\x03\x8a\xb5\x18\x02H\x01\x12#\n\tremaining\x18\x65 \x01(\rB\x10\x92?\x02\x38 \x8a\xb5\x18\x07\x08\x03\x10\xe8\x07(\x01\x42\x0c\n\nconstraint\"i\n\x1c\x44\x65precatedDigitalConstraints\x12I\n\x0b\x63onstraints\x18\x01 \x03(\x0b\x32-.blox.Constraints.DeprecatedDigitalConstraintB\x05\x92?\x02\x10\x08\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Constraints_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _VALUECONSTRAINT.fields_by_name['value']._options = None
  _VALUECONSTRAINT.fields_by_name['value']._serialized_options = b'\222?\0028 \212\265\030\005\020\200 x\001'
  _VALUECONSTRAINT.fields_by_name['enabled']._options = None
  _VALUECONSTRAINT.fields_by_name['enabled']._serialized_options = b'\212\265\030\002x\001'
  _VALUECONSTRAINT.fields_by_name['limiting']._options = None
  _VALUECONSTRAINT.fields_by_name['limiting']._serialized_options = b'\212\265\030\002(\001'
  _BALANCEDCONSTRAINT.fields_by_name['balancerId']._options = None
  _BALANCEDCONSTRAINT.fields_by_name['balancerId']._serialized_options = b'\212\265\030\004\030\007x\001'
  _BALANCEDCONSTRAINT.fields_by_name['granted']._options = None
  _BALANCEDCONSTRAINT.fields_by_name['granted']._serialized_options = b'\212\265\030\005\020\200 (\001'
  _BALANCEDCONSTRAINT.fields_by_name['enabled']._options = None
  _BALANCEDCONSTRAINT.fields_by_name['enabled']._serialized_options = b'\212\265\030\002x\001'
  _BALANCEDCONSTRAINT.fields_by_name['limiting']._options = None
  _BALANCEDCONSTRAINT.fields_by_name['limiting']._serialized_options = b'\212\265\030\002(\001'
  _BALANCEDCONSTRAINT.fields_by_name['id']._options = None
  _BALANCEDCONSTRAINT.fields_by_name['id']._serialized_options = b'\222?\002\030\003\212\265\030\002H\001'
  _DURATIONCONSTRAINT.fields_by_name['duration']._options = None
  _DURATIONCONSTRAINT.fields_by_name['duration']._serialized_options = b'\222?\0028 \212\265\030\007\010\003\020\350\007x\001'
  _DURATIONCONSTRAINT.fields_by_name['enabled']._options = None
  _DURATIONCONSTRAINT.fields_by_name['enabled']._serialized_options = b'\212\265\030\002x\001'
  _DURATIONCONSTRAINT.fields_by_name['limiting']._options = None
  _DURATIONCONSTRAINT.fields_by_name['limiting']._serialized_options = b'\212\265\030\002(\001'
  _DURATIONCONSTRAINT.fields_by_name['remaining']._options = None
  _DURATIONCONSTRAINT.fields_by_name['remaining']._serialized_options = b'\222?\0028 \212\265\030\007\010\003\020\350\007(\001'
  _MUTEXEDCONSTRAINT.fields_by_name['mutexId']._options = None
  _MUTEXEDCONSTRAINT.fields_by_name['mutexId']._serialized_options = b'\212\265\030\004\030\010x\001'
  _MUTEXEDCONSTRAINT.fields_by_name['extraHoldTime']._options = None
  _MUTEXEDCONSTRAINT.fields_by_name['extraHoldTime']._serialized_options = b'\222?\0028 \212\265\030\007\010\003\020\350\007x\001'
  _MUTEXEDCONSTRAINT.fields_by_name['hasLock']._options = None
  _MUTEXEDCONSTRAINT.fields_by_name['hasLock']._serialized_options = b'\212\265\030\002(\001'
  _MUTEXEDCONSTRAINT.fields_by_name['enabled']._options = None
  _MUTEXEDCONSTRAINT.fields_by_name['enabled']._serialized_options = b'\212\265\030\002x\001'
  _MUTEXEDCONSTRAINT.fields_by_name['limiting']._options = None
  _MUTEXEDCONSTRAINT.fields_by_name['limiting']._serialized_options = b'\212\265\030\002(\001'
  _MUTEXEDCONSTRAINT.fields_by_name['remaining']._options = None
  _MUTEXEDCONSTRAINT.fields_by_name['remaining']._serialized_options = b'\222?\0028 \212\265\030\007\010\003\020\350\007(\001'
  _MUTEXEDCONSTRAINT.fields_by_name['hasCustomHoldTime']._options = None
  _MUTEXEDCONSTRAINT.fields_by_name['hasCustomHoldTime']._serialized_options = b'\222?\002\030\003\212\265\030\002H\001'
  _ANALOGCONSTRAINTS.fields_by_name['min']._options = None
  _ANALOGCONSTRAINTS.fields_by_name['min']._serialized_options = b'\212\265\030\002x\001'
  _ANALOGCONSTRAINTS.fields_by_name['max']._options = None
  _ANALOGCONSTRAINTS.fields_by_name['max']._serialized_options = b'\212\265\030\002x\001'
  _ANALOGCONSTRAINTS.fields_by_name['balanced']._options = None
  _ANALOGCONSTRAINTS.fields_by_name['balanced']._serialized_options = b'\212\265\030\002x\001'
  _DIGITALCONSTRAINTS.fields_by_name['minOff']._options = None
  _DIGITALCONSTRAINTS.fields_by_name['minOff']._serialized_options = b'\212\265\030\002x\001'
  _DIGITALCONSTRAINTS.fields_by_name['minOn']._options = None
  _DIGITALCONSTRAINTS.fields_by_name['minOn']._serialized_options = b'\212\265\030\002x\001'
  _DIGITALCONSTRAINTS.fields_by_name['delayedOff']._options = None
  _DIGITALCONSTRAINTS.fields_by_name['delayedOff']._serialized_options = b'\212\265\030\002x\001'
  _DIGITALCONSTRAINTS.fields_by_name['delayedOn']._options = None
  _DIGITALCONSTRAINTS.fields_by_name['delayedOn']._serialized_options = b'\212\265\030\002x\001'
  _DIGITALCONSTRAINTS.fields_by_name['mutexed']._options = None
  _DIGITALCONSTRAINTS.fields_by_name['mutexed']._serialized_options = b'\212\265\030\002x\001'
  _DEPRECATEDANALOGCONSTRAINT.fields_by_name['min']._options = None
  _DEPRECATEDANALOGCONSTRAINT.fields_by_name['min']._serialized_options = b'\222?\0028 \212\265\030\003\020\200 '
  _DEPRECATEDANALOGCONSTRAINT.fields_by_name['max']._options = None
  _DEPRECATEDANALOGCONSTRAINT.fields_by_name['max']._serialized_options = b'\222?\0028 \212\265\030\003\020\200 '
  _DEPRECATEDANALOGCONSTRAINT.fields_by_name['limiting']._options = None
  _DEPRECATEDANALOGCONSTRAINT.fields_by_name['limiting']._serialized_options = b'\212\265\030\002(\001'
  _DEPRECATEDANALOGCONSTRAINTS.fields_by_name['constraints']._options = None
  _DEPRECATEDANALOGCONSTRAINTS.fields_by_name['constraints']._serialized_options = b'\222?\002\020\010'
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['minOff']._options = None
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['minOff']._serialized_options = b'\222?\0028 \212\265\030\005\010\003\020\350\007'
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['minOn']._options = None
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['minOn']._serialized_options = b'\222?\0028 \212\265\030\005\010\003\020\350\007'
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['delayedOff']._options = None
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['delayedOff']._serialized_options = b'\222?\0028 \212\265\030\005\010\003\020\350\007'
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['delayedOn']._options = None
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['delayedOn']._serialized_options = b'\222?\0028 \212\265\030\005\010\003\020\350\007'
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['mutex']._options = None
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['mutex']._serialized_options = b'\212\265\030\002\030\010'
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['limiting']._options = None
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['limiting']._serialized_options = b'\222?\002\030\003\212\265\030\002H\001'
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['remaining']._options = None
  _DEPRECATEDDIGITALCONSTRAINT.fields_by_name['remaining']._serialized_options = b'\222?\0028 \212\265\030\007\010\003\020\350\007(\001'
  _DEPRECATEDDIGITALCONSTRAINTS.fields_by_name['constraints']._options = None
  _DEPRECATEDDIGITALCONSTRAINTS.fields_by_name['constraints']._serialized_options = b'\222?\002\020\010'
  _globals['_VALUECONSTRAINT']._serialized_start=69
  _globals['_VALUECONSTRAINT']._serialized_end=168
  _globals['_BALANCEDCONSTRAINT']._serialized_start=171
  _globals['_BALANCEDCONSTRAINT']._serialized_end=325
  _globals['_DURATIONCONSTRAINT']._serialized_start=328
  _globals['_DURATIONCONSTRAINT']._serialized_end=472
  _globals['_MUTEXEDCONSTRAINT']._serialized_start=475
  _globals['_MUTEXEDCONSTRAINT']._serialized_end=715
  _globals['_ANALOGCONSTRAINTS']._serialized_start=718
  _globals['_ANALOGCONSTRAINTS']._serialized_end=913
  _globals['_DIGITALCONSTRAINTS']._serialized_start=916
  _globals['_DIGITALCONSTRAINTS']._serialized_end=1252
  _globals['_DEPRECATEDANALOGCONSTRAINT']._serialized_start=1255
  _globals['_DEPRECATEDANALOGCONSTRAINT']._serialized_end=1439
  _globals['_DEPRECATEDANALOGCONSTRAINTS']._serialized_start=1441
  _globals['_DEPRECATEDANALOGCONSTRAINTS']._serialized_end=1544
  _globals['_DEPRECATEDDIGITALCONSTRAINT']._serialized_start=1547
  _globals['_DEPRECATEDDIGITALCONSTRAINT']._serialized_end=1881
  _globals['_DEPRECATEDDIGITALCONSTRAINTS']._serialized_start=1883
  _globals['_DEPRECATEDDIGITALCONSTRAINTS']._serialized_end=1988
# @@protoc_insertion_point(module_scope)

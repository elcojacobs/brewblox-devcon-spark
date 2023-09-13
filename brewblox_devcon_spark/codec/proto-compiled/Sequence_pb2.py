# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Sequence.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import IoArray_pb2 as IoArray__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eSequence.proto\x12\rblox.Sequence\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\rIoArray.proto\"\x17\n\x07\x43omment\x12\x0c\n\x04text\x18\x01 \x01(\t\"\t\n\x07Restart\",\n\rEnableDisable\x12\x1b\n\x06target\x18\x01 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x18\x0f\"\x06\n\x04Wait\"-\n\x0cWaitDuration\x12\x1d\n\x08\x64uration\x18\x01 \x01(\rB\x0b\x92?\x02\x38 \x8a\xb5\x18\x02\x08\x03\"&\n\tWaitUntil\x12\x19\n\x04time\x18\x01 \x01(\rB\x0b\x92?\x02\x38 \x8a\xb5\x18\x02X\x01\"q\n\x14WaitTemperatureRange\x12\x1b\n\x06target\x18\x01 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x18\x02\x12\x1d\n\x05lower\x18\x02 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x08\x01\x10\x80 \x12\x1d\n\x05upper\x18\x03 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x08\x01\x10\x80 \"U\n\x17WaitTemperatureBoundary\x12\x1b\n\x06target\x18\x01 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x18\x02\x12\x1d\n\x05value\x18\x02 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x08\x01\x10\x80 \"K\n\x0bSetSetpoint\x12\x1b\n\x06target\x18\x01 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x18\x04\x12\x1f\n\x07setting\x18\x02 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x08\x01\x10\x80 \"N\n\x0cWaitSetpoint\x12\x1b\n\x06target\x18\x01 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x18\x04\x12!\n\tprecision\x18\x02 \x01(\x11\x42\x0e\x92?\x02\x38 \x8a\xb5\x18\x05\x08\x06\x10\x80 \"V\n\nSetDigital\x12\x1b\n\x06target\x18\x01 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x18\x06\x12+\n\x07setting\x18\x02 \x01(\x0e\x32\x1a.blox.IoArray.DigitalState\"*\n\x0bWaitDigital\x12\x1b\n\x06target\x18\x01 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x18\x06\"Z\n\x10WaitDigitalState\x12\x1b\n\x06target\x18\x01 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x18\x1b\x12)\n\x05state\x18\x02 \x01(\x0e\x32\x1a.blox.IoArray.DigitalState\"D\n\x06SetPwm\x12\x1b\n\x06target\x18\x01 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x18\x05\x12\x1d\n\x07setting\x18\x02 \x01(\x11\x42\x0c\x92?\x02\x38 \x8a\xb5\x18\x03\x10\x80 \"-\n\rTargetProfile\x12\x1c\n\x06target\x18\x01 \x01(\rB\x0c\x92?\x02\x38\x10\x8a\xb5\x18\x03\x18\xb7\x02\".\n\x0eTargetSequence\x12\x1c\n\x06target\x18\x01 \x01(\rB\x0c\x92?\x02\x38\x10\x8a\xb5\x18\x03\x18\xc6\x02\"\xd0\n\n\x0bInstruction\x12)\n\x07RESTART\x18\x01 \x01(\x0b\x32\x16.blox.Sequence.RestartH\x00\x12.\n\x06\x45NABLE\x18\x02 \x01(\x0b\x32\x1c.blox.Sequence.EnableDisableH\x00\x12/\n\x07\x44ISABLE\x18\x03 \x01(\x0b\x32\x1c.blox.Sequence.EnableDisableH\x00\x12#\n\x04WAIT\x18\x14 \x01(\x0b\x32\x13.blox.Sequence.WaitH\x00\x12\x34\n\rWAIT_DURATION\x18\x04 \x01(\x0b\x32\x1b.blox.Sequence.WaitDurationH\x00\x12.\n\nWAIT_UNTIL\x18\x05 \x01(\x0b\x32\x18.blox.Sequence.WaitUntilH\x00\x12@\n\x11WAIT_TEMP_BETWEEN\x18\x06 \x01(\x0b\x32#.blox.Sequence.WaitTemperatureRangeH\x00\x12\x44\n\x15WAIT_TEMP_NOT_BETWEEN\x18\x07 \x01(\x0b\x32#.blox.Sequence.WaitTemperatureRangeH\x00\x12\x43\n\x14WAIT_TEMP_UNEXPECTED\x18\x08 \x01(\x0b\x32#.blox.Sequence.WaitTemperatureRangeH\x00\x12\x41\n\x0fWAIT_TEMP_ABOVE\x18\t \x01(\x0b\x32&.blox.Sequence.WaitTemperatureBoundaryH\x00\x12\x41\n\x0fWAIT_TEMP_BELOW\x18\n \x01(\x0b\x32&.blox.Sequence.WaitTemperatureBoundaryH\x00\x12\x32\n\x0cSET_SETPOINT\x18\x0b \x01(\x0b\x32\x1a.blox.Sequence.SetSetpointH\x00\x12\x34\n\rWAIT_SETPOINT\x18\x0c \x01(\x0b\x32\x1b.blox.Sequence.WaitSetpointH\x00\x12:\n\x13WAIT_SETPOINT_ABOVE\x18\x15 \x01(\x0b\x32\x1b.blox.Sequence.WaitSetpointH\x00\x12:\n\x13WAIT_SETPOINT_BELOW\x18\x16 \x01(\x0b\x32\x1b.blox.Sequence.WaitSetpointH\x00\x12\x30\n\x0bSET_DIGITAL\x18\r \x01(\x0b\x32\x19.blox.Sequence.SetDigitalH\x00\x12\x32\n\x0cWAIT_DIGITAL\x18\x0e \x01(\x0b\x32\x1a.blox.Sequence.WaitDigitalH\x00\x12>\n\x13WAIT_DIGITAL_EQUALS\x18\x17 \x01(\x0b\x32\x1f.blox.Sequence.WaitDigitalStateH\x00\x12(\n\x07SET_PWM\x18\x0f \x01(\x0b\x32\x15.blox.Sequence.SetPwmH\x00\x12\x35\n\rSTART_PROFILE\x18\x10 \x01(\x0b\x32\x1c.blox.Sequence.TargetProfileH\x00\x12\x34\n\x0cWAIT_PROFILE\x18\x11 \x01(\x0b\x32\x1c.blox.Sequence.TargetProfileH\x00\x12\x37\n\x0eSTART_SEQUENCE\x18\x12 \x01(\x0b\x32\x1d.blox.Sequence.TargetSequenceH\x00\x12\x36\n\rWAIT_SEQUENCE\x18\x13 \x01(\x0b\x32\x1d.blox.Sequence.TargetSequenceH\x00\x12*\n\x07\x43OMMENT\x18\xc8\x01 \x01(\x0b\x32\x16.blox.Sequence.CommentH\x00:\x06\x92?\x03\xb0\x01\x01\x42\x13\n\x11instruction_oneof\"\xa7\x03\n\x05\x42lock\x12\x17\n\x07\x65nabled\x18\x01 \x01(\x08\x42\x06\x8a\xb5\x18\x02\x30\x01\x12\x30\n\x0cinstructions\x18\x02 \x03(\x0b\x32\x1a.blox.Sequence.Instruction\x12\x15\n\roverrideState\x18\x03 \x01(\x08\x12&\n\x11\x61\x63tiveInstruction\x18\x04 \x01(\rB\x0b\x92?\x02\x38\x10\x8a\xb5\x18\x02\x30\x01\x12\x35\n\x06status\x18\x08 \x01(\x0e\x32\x1d.blox.Sequence.SequenceStatusB\x06\x8a\xb5\x18\x02(\x01\x12\x33\n\x05\x65rror\x18\t \x01(\x0e\x32\x1c.blox.Sequence.SequenceErrorB\x06\x8a\xb5\x18\x02(\x01\x12#\n\x07\x65lapsed\x18\n \x01(\rB\x12\x92?\x02\x38 \x8a\xb5\x18\t\x08\x03\x10\xe8\x07(\x01\x30\x01\x12/\n\x1a\x61\x63tiveInstructionStartedAt\x18\x05 \x01(\rB\x0b\x92?\x02\x18\x03\x8a\xb5\x18\x02H\x01\x12\x1f\n\ndisabledAt\x18\x06 \x01(\rB\x0b\x92?\x02\x18\x03\x8a\xb5\x18\x02H\x01\x12%\n\x10\x64isabledDuration\x18\x07 \x01(\rB\x0b\x92?\x02\x18\x03\x8a\xb5\x18\x02H\x01:\n\x8a\xb5\x18\x06\x18\xc6\x02J\x01\x0f*l\n\x0eSequenceStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x08\n\x04NEXT\x10\x03\x12\x08\n\x04WAIT\x10\x04\x12\x07\n\x03\x45ND\x10\x05\x12\x0b\n\x07RESTART\x10\x06\x12\t\n\x05\x45RROR\x10\x07*\x8c\x01\n\rSequenceError\x12\x08\n\x04NONE\x10\x00\x12\x14\n\x10INVALID_ARGUMENT\x10\x01\x12\x12\n\x0eINVALID_TARGET\x10\x02\x12\x13\n\x0fINACTIVE_TARGET\x10\x03\x12\x13\n\x0f\x44ISABLED_TARGET\x10\x04\x12\x1d\n\x19SYSTEM_TIME_NOT_AVAILABLE\x10\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Sequence_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENABLEDISABLE.fields_by_name['target']._options = None
  _ENABLEDISABLE.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\002\030\017'
  _WAITDURATION.fields_by_name['duration']._options = None
  _WAITDURATION.fields_by_name['duration']._serialized_options = b'\222?\0028 \212\265\030\002\010\003'
  _WAITUNTIL.fields_by_name['time']._options = None
  _WAITUNTIL.fields_by_name['time']._serialized_options = b'\222?\0028 \212\265\030\002X\001'
  _WAITTEMPERATURERANGE.fields_by_name['target']._options = None
  _WAITTEMPERATURERANGE.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\002\030\002'
  _WAITTEMPERATURERANGE.fields_by_name['lower']._options = None
  _WAITTEMPERATURERANGE.fields_by_name['lower']._serialized_options = b'\222?\0028 \212\265\030\005\010\001\020\200 '
  _WAITTEMPERATURERANGE.fields_by_name['upper']._options = None
  _WAITTEMPERATURERANGE.fields_by_name['upper']._serialized_options = b'\222?\0028 \212\265\030\005\010\001\020\200 '
  _WAITTEMPERATUREBOUNDARY.fields_by_name['target']._options = None
  _WAITTEMPERATUREBOUNDARY.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\002\030\002'
  _WAITTEMPERATUREBOUNDARY.fields_by_name['value']._options = None
  _WAITTEMPERATUREBOUNDARY.fields_by_name['value']._serialized_options = b'\222?\0028 \212\265\030\005\010\001\020\200 '
  _SETSETPOINT.fields_by_name['target']._options = None
  _SETSETPOINT.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\002\030\004'
  _SETSETPOINT.fields_by_name['setting']._options = None
  _SETSETPOINT.fields_by_name['setting']._serialized_options = b'\222?\0028 \212\265\030\005\010\001\020\200 '
  _WAITSETPOINT.fields_by_name['target']._options = None
  _WAITSETPOINT.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\002\030\004'
  _WAITSETPOINT.fields_by_name['precision']._options = None
  _WAITSETPOINT.fields_by_name['precision']._serialized_options = b'\222?\0028 \212\265\030\005\010\006\020\200 '
  _SETDIGITAL.fields_by_name['target']._options = None
  _SETDIGITAL.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\002\030\006'
  _WAITDIGITAL.fields_by_name['target']._options = None
  _WAITDIGITAL.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\002\030\006'
  _WAITDIGITALSTATE.fields_by_name['target']._options = None
  _WAITDIGITALSTATE.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\002\030\033'
  _SETPWM.fields_by_name['target']._options = None
  _SETPWM.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\002\030\005'
  _SETPWM.fields_by_name['setting']._options = None
  _SETPWM.fields_by_name['setting']._serialized_options = b'\222?\0028 \212\265\030\003\020\200 '
  _TARGETPROFILE.fields_by_name['target']._options = None
  _TARGETPROFILE.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\003\030\267\002'
  _TARGETSEQUENCE.fields_by_name['target']._options = None
  _TARGETSEQUENCE.fields_by_name['target']._serialized_options = b'\222?\0028\020\212\265\030\003\030\306\002'
  _INSTRUCTION._options = None
  _INSTRUCTION._serialized_options = b'\222?\003\260\001\001'
  _BLOCK.fields_by_name['enabled']._options = None
  _BLOCK.fields_by_name['enabled']._serialized_options = b'\212\265\030\0020\001'
  _BLOCK.fields_by_name['activeInstruction']._options = None
  _BLOCK.fields_by_name['activeInstruction']._serialized_options = b'\222?\0028\020\212\265\030\0020\001'
  _BLOCK.fields_by_name['status']._options = None
  _BLOCK.fields_by_name['status']._serialized_options = b'\212\265\030\002(\001'
  _BLOCK.fields_by_name['error']._options = None
  _BLOCK.fields_by_name['error']._serialized_options = b'\212\265\030\002(\001'
  _BLOCK.fields_by_name['elapsed']._options = None
  _BLOCK.fields_by_name['elapsed']._serialized_options = b'\222?\0028 \212\265\030\t\010\003\020\350\007(\0010\001'
  _BLOCK.fields_by_name['activeInstructionStartedAt']._options = None
  _BLOCK.fields_by_name['activeInstructionStartedAt']._serialized_options = b'\222?\002\030\003\212\265\030\002H\001'
  _BLOCK.fields_by_name['disabledAt']._options = None
  _BLOCK.fields_by_name['disabledAt']._serialized_options = b'\222?\002\030\003\212\265\030\002H\001'
  _BLOCK.fields_by_name['disabledDuration']._options = None
  _BLOCK.fields_by_name['disabledDuration']._serialized_options = b'\222?\002\030\003\212\265\030\002H\001'
  _BLOCK._options = None
  _BLOCK._serialized_options = b'\212\265\030\006\030\306\002J\001\017'
  _globals['_SEQUENCESTATUS']._serialized_start=2792
  _globals['_SEQUENCESTATUS']._serialized_end=2900
  _globals['_SEQUENCEERROR']._serialized_start=2903
  _globals['_SEQUENCEERROR']._serialized_end=3043
  _globals['_COMMENT']._serialized_start=78
  _globals['_COMMENT']._serialized_end=101
  _globals['_RESTART']._serialized_start=103
  _globals['_RESTART']._serialized_end=112
  _globals['_ENABLEDISABLE']._serialized_start=114
  _globals['_ENABLEDISABLE']._serialized_end=158
  _globals['_WAIT']._serialized_start=160
  _globals['_WAIT']._serialized_end=166
  _globals['_WAITDURATION']._serialized_start=168
  _globals['_WAITDURATION']._serialized_end=213
  _globals['_WAITUNTIL']._serialized_start=215
  _globals['_WAITUNTIL']._serialized_end=253
  _globals['_WAITTEMPERATURERANGE']._serialized_start=255
  _globals['_WAITTEMPERATURERANGE']._serialized_end=368
  _globals['_WAITTEMPERATUREBOUNDARY']._serialized_start=370
  _globals['_WAITTEMPERATUREBOUNDARY']._serialized_end=455
  _globals['_SETSETPOINT']._serialized_start=457
  _globals['_SETSETPOINT']._serialized_end=532
  _globals['_WAITSETPOINT']._serialized_start=534
  _globals['_WAITSETPOINT']._serialized_end=612
  _globals['_SETDIGITAL']._serialized_start=614
  _globals['_SETDIGITAL']._serialized_end=700
  _globals['_WAITDIGITAL']._serialized_start=702
  _globals['_WAITDIGITAL']._serialized_end=744
  _globals['_WAITDIGITALSTATE']._serialized_start=746
  _globals['_WAITDIGITALSTATE']._serialized_end=836
  _globals['_SETPWM']._serialized_start=838
  _globals['_SETPWM']._serialized_end=906
  _globals['_TARGETPROFILE']._serialized_start=908
  _globals['_TARGETPROFILE']._serialized_end=953
  _globals['_TARGETSEQUENCE']._serialized_start=955
  _globals['_TARGETSEQUENCE']._serialized_end=1001
  _globals['_INSTRUCTION']._serialized_start=1004
  _globals['_INSTRUCTION']._serialized_end=2364
  _globals['_BLOCK']._serialized_start=2367
  _globals['_BLOCK']._serialized_end=2790
# @@protoc_insertion_point(module_scope)

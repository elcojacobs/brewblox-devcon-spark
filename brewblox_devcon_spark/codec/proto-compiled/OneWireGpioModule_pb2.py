# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OneWireGpioModule.proto

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
  name='OneWireGpioModule.proto',
  package='blox.OneWireGpioModule',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17OneWireGpioModule.proto\x12\x16\x62lox.OneWireGpioModule\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xfc\x01\n\x11GpioModuleChannel\x12\x11\n\x02id\x18\x01 \x01(\rB\x05\x92?\x02\x38\x08\x12:\n\ndeviceType\x18\x02 \x01(\x0e\x32&.blox.OneWireGpioModule.GpioDeviceType\x12\x1d\n\x08pinsMask\x18\x03 \x01(\rB\x0b\x8a\xb5\x18\x02P\x01\x92?\x02\x38\x08\x12\x14\n\x05width\x18\x04 \x01(\rB\x05\x92?\x02\x38\x08\x12\x13\n\x04name\x18\x05 \x01(\tB\x05\x92?\x02\x08 \x12\'\n\x0c\x63\x61pabilities\x18\x06 \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x02P\x01\x92?\x02\x38\x10\x12%\n\tclaimedBy\x18\x07 \x01(\rB\x12\x8a\xb5\x18\x03\x18\xff\x01\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\"\xac\x05\n\x05\x42lock\x12\x42\n\x08\x63hannels\x18\x01 \x03(\x0b\x32).blox.OneWireGpioModule.GpioModuleChannelB\x05\x92?\x02\x10\x08\x12\x1d\n\x0emodulePosition\x18\x02 \x01(\rB\x05\x92?\x02\x38\x08\x12!\n\x0cmoduleStatus\x18\x03 \x01(\rB\x0b\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12(\n\rpullUpDesired\x18\x04 \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12\'\n\x0cpullUpStatus\x18\x05 \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12+\n\x10pullUpWhenActive\x18\x06 \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12-\n\x12pullUpWhenInactive\x18\x07 \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12*\n\x0fpullDownDesired\x18\x08 \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12)\n\x0epullDownStatus\x18\t \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12-\n\x12pullDownWhenActive\x18\n \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12/\n\x14pullDownWhenInactive\x18\x0b \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12&\n\x0boverCurrent\x18\x0c \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12#\n\x08openLoad\x18\r \x01(\rB\x11\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x08\x8a\xb5\x18\x02P\x01\x12\x18\n\x10useExternalPower\x18\x0e \x01(\x08\x12\x13\n\x0b\x63learFaults\x18  \x01(\x08\x12&\n\x11moduleStatusClear\x18Z \x01(\rB\x0b\x8a\xb5\x18\x02H\x01\x92?\x02\x18\x03:\x13\x8a\xb5\x18\x03\x18\xc5\x02\x8a\xb5\x18\x02H\n\x8a\xb5\x18\x02H\x0c*\x8e\x05\n\x0eGpioDeviceType\x12\x11\n\rGPIO_DEV_NONE\x10\x00\x12\x13\n\x0fGPIO_DEV_SSR_2P\x10\x01\x12\x13\n\x0fGPIO_DEV_SSR_1P\x10\x02\x12 \n\x1cGPIO_DEV_MECHANICAL_RELAY_2P\x10\x03\x12*\n&GPIO_DEV_MECHANICAL_RELAY_1P_HIGH_SIDE\x10\x04\x12)\n%GPIO_DEV_MECHANICAL_RELAY_1P_LOW_SIDE\x10\x05\x12\x14\n\x10GPIO_DEV_COIL_2P\x10\x06\x12\"\n\x1eGPIO_DEV_COIL_2P_BIDIRECTIONAL\x10\x07\x12\x1e\n\x1aGPIO_DEV_COIL_1P_HIGH_SIDE\x10\x08\x12\x1d\n\x19GPIO_DEV_COIL_1P_LOW_SIDE\x10\t\x12\x15\n\x11GPIO_DEV_MOTOR_2P\x10\n\x12#\n\x1fGPIO_DEV_MOTOR_2P_BIDIRECTIONAL\x10\x0b\x12\x1f\n\x1bGPIO_DEV_MOTOR_1P_HIGH_SIDE\x10\x0c\x12\x1e\n\x1aGPIO_DEV_MOTOR_1P_LOW_SIDE\x10\r\x12\x16\n\x12GPIO_DEV_SWITCH_2P\x10\x0e\x12#\n\x1fGPIO_DEV_SWITCH_1P_EXTERNAL_GND\x10\x0f\x12#\n\x1fGPIO_DEV_SWITCH_1P_EXTERNAL_PWR\x10\x10\x12\x15\n\x11GPIO_DEV_POWER_1P\x10\x11\x12!\n\x1dGPIO_DEV_POWER_1P_LOAD_DETECT\x10\x12\x12\x13\n\x0fGPIO_DEV_GND_1P\x10\x13\x12\x1f\n\x1bGPIO_DEV_GND_1P_LOAD_DETECT\x10\x14*\x8a\x02\n\x0eGpioErrorFlags\x12\x11\n\rGPIO_ERR_NONE\x10\x00\x12\x1b\n\x17GPIO_ERR_POWER_ON_RESET\x10\x01\x12\x18\n\x14GPIO_ERR_OVERVOLTAGE\x10\x02\x12\x19\n\x15GPIO_ERR_UNDERVOLTAGE\x10\x04\x12\x18\n\x14GPIO_ERR_OVERCURRENT\x10\x08\x12\x16\n\x12GPIO_ERR_OPEN_LOAD\x10\x10\x12$\n GPIO_ERR_OVERTEMPERATURE_WARNING\x10 \x12\"\n\x1eGPIO_ERR_OVERTEMPERATURE_ERROR\x10@\x12\x17\n\x12GPIO_ERR_SPI_ERROR\x10\x80\x01\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])

_GPIODEVICETYPE = _descriptor.EnumDescriptor(
  name='GpioDeviceType',
  full_name='blox.OneWireGpioModule.GpioDeviceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_SSR_2P', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_SSR_1P', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_MECHANICAL_RELAY_2P', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_MECHANICAL_RELAY_1P_HIGH_SIDE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_MECHANICAL_RELAY_1P_LOW_SIDE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_COIL_2P', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_COIL_2P_BIDIRECTIONAL', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_COIL_1P_HIGH_SIDE', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_COIL_1P_LOW_SIDE', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_MOTOR_2P', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_MOTOR_2P_BIDIRECTIONAL', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_MOTOR_1P_HIGH_SIDE', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_MOTOR_1P_LOW_SIDE', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_SWITCH_2P', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_SWITCH_1P_EXTERNAL_GND', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_SWITCH_1P_EXTERNAL_PWR', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_POWER_1P', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_POWER_1P_LOAD_DETECT', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_GND_1P', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_DEV_GND_1P_LOAD_DETECT', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1024,
  serialized_end=1678,
)
_sym_db.RegisterEnumDescriptor(_GPIODEVICETYPE)

GpioDeviceType = enum_type_wrapper.EnumTypeWrapper(_GPIODEVICETYPE)
_GPIOERRORFLAGS = _descriptor.EnumDescriptor(
  name='GpioErrorFlags',
  full_name='blox.OneWireGpioModule.GpioErrorFlags',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GPIO_ERR_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_ERR_POWER_ON_RESET', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_ERR_OVERVOLTAGE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_ERR_UNDERVOLTAGE', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_ERR_OVERCURRENT', index=4, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_ERR_OPEN_LOAD', index=5, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_ERR_OVERTEMPERATURE_WARNING', index=6, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_ERR_OVERTEMPERATURE_ERROR', index=7, number=64,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPIO_ERR_SPI_ERROR', index=8, number=128,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1681,
  serialized_end=1947,
)
_sym_db.RegisterEnumDescriptor(_GPIOERRORFLAGS)

GpioErrorFlags = enum_type_wrapper.EnumTypeWrapper(_GPIOERRORFLAGS)
GPIO_DEV_NONE = 0
GPIO_DEV_SSR_2P = 1
GPIO_DEV_SSR_1P = 2
GPIO_DEV_MECHANICAL_RELAY_2P = 3
GPIO_DEV_MECHANICAL_RELAY_1P_HIGH_SIDE = 4
GPIO_DEV_MECHANICAL_RELAY_1P_LOW_SIDE = 5
GPIO_DEV_COIL_2P = 6
GPIO_DEV_COIL_2P_BIDIRECTIONAL = 7
GPIO_DEV_COIL_1P_HIGH_SIDE = 8
GPIO_DEV_COIL_1P_LOW_SIDE = 9
GPIO_DEV_MOTOR_2P = 10
GPIO_DEV_MOTOR_2P_BIDIRECTIONAL = 11
GPIO_DEV_MOTOR_1P_HIGH_SIDE = 12
GPIO_DEV_MOTOR_1P_LOW_SIDE = 13
GPIO_DEV_SWITCH_2P = 14
GPIO_DEV_SWITCH_1P_EXTERNAL_GND = 15
GPIO_DEV_SWITCH_1P_EXTERNAL_PWR = 16
GPIO_DEV_POWER_1P = 17
GPIO_DEV_POWER_1P_LOAD_DETECT = 18
GPIO_DEV_GND_1P = 19
GPIO_DEV_GND_1P_LOAD_DETECT = 20
GPIO_ERR_NONE = 0
GPIO_ERR_POWER_ON_RESET = 1
GPIO_ERR_OVERVOLTAGE = 2
GPIO_ERR_UNDERVOLTAGE = 4
GPIO_ERR_OVERCURRENT = 8
GPIO_ERR_OPEN_LOAD = 16
GPIO_ERR_OVERTEMPERATURE_WARNING = 32
GPIO_ERR_OVERTEMPERATURE_ERROR = 64
GPIO_ERR_SPI_ERROR = 128



_GPIOMODULECHANNEL = _descriptor.Descriptor(
  name='GpioModuleChannel',
  full_name='blox.OneWireGpioModule.GpioModuleChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='blox.OneWireGpioModule.GpioModuleChannel.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceType', full_name='blox.OneWireGpioModule.GpioModuleChannel.deviceType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pinsMask', full_name='blox.OneWireGpioModule.GpioModuleChannel.pinsMask', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002P\001\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='blox.OneWireGpioModule.GpioModuleChannel.width', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='blox.OneWireGpioModule.GpioModuleChannel.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002\010 ', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='capabilities', full_name='blox.OneWireGpioModule.GpioModuleChannel.capabilities', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\212\265\030\002P\001\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claimedBy', full_name='blox.OneWireGpioModule.GpioModuleChannel.claimedBy', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\003\030\377\001\212\265\030\002(\001\222?\0028\020', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=82,
  serialized_end=334,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blox.OneWireGpioModule.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='blox.OneWireGpioModule.Block.channels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\002\020\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modulePosition', full_name='blox.OneWireGpioModule.Block.modulePosition', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\0028\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='moduleStatus', full_name='blox.OneWireGpioModule.Block.moduleStatus', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pullUpDesired', full_name='blox.OneWireGpioModule.Block.pullUpDesired', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pullUpStatus', full_name='blox.OneWireGpioModule.Block.pullUpStatus', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pullUpWhenActive', full_name='blox.OneWireGpioModule.Block.pullUpWhenActive', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pullUpWhenInactive', full_name='blox.OneWireGpioModule.Block.pullUpWhenInactive', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pullDownDesired', full_name='blox.OneWireGpioModule.Block.pullDownDesired', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pullDownStatus', full_name='blox.OneWireGpioModule.Block.pullDownStatus', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pullDownWhenActive', full_name='blox.OneWireGpioModule.Block.pullDownWhenActive', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pullDownWhenInactive', full_name='blox.OneWireGpioModule.Block.pullDownWhenInactive', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='overCurrent', full_name='blox.OneWireGpioModule.Block.overCurrent', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='openLoad', full_name='blox.OneWireGpioModule.Block.openLoad', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\010\212\265\030\002P\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='useExternalPower', full_name='blox.OneWireGpioModule.Block.useExternalPower', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clearFaults', full_name='blox.OneWireGpioModule.Block.clearFaults', index=14,
      number=32, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='moduleStatusClear', full_name='blox.OneWireGpioModule.Block.moduleStatusClear', index=15,
      number=90, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002H\001\222?\002\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\305\002\212\265\030\002H\n\212\265\030\002H\014',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=337,
  serialized_end=1021,
)

_GPIOMODULECHANNEL.fields_by_name['deviceType'].enum_type = _GPIODEVICETYPE
_BLOCK.fields_by_name['channels'].message_type = _GPIOMODULECHANNEL
DESCRIPTOR.message_types_by_name['GpioModuleChannel'] = _GPIOMODULECHANNEL
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.enum_types_by_name['GpioDeviceType'] = _GPIODEVICETYPE
DESCRIPTOR.enum_types_by_name['GpioErrorFlags'] = _GPIOERRORFLAGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GpioModuleChannel = _reflection.GeneratedProtocolMessageType('GpioModuleChannel', (_message.Message,), {
  'DESCRIPTOR' : _GPIOMODULECHANNEL,
  '__module__' : 'OneWireGpioModule_pb2'
  # @@protoc_insertion_point(class_scope:blox.OneWireGpioModule.GpioModuleChannel)
  })
_sym_db.RegisterMessage(GpioModuleChannel)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'OneWireGpioModule_pb2'
  # @@protoc_insertion_point(class_scope:blox.OneWireGpioModule.Block)
  })
_sym_db.RegisterMessage(Block)


_GPIOMODULECHANNEL.fields_by_name['id']._options = None
_GPIOMODULECHANNEL.fields_by_name['pinsMask']._options = None
_GPIOMODULECHANNEL.fields_by_name['width']._options = None
_GPIOMODULECHANNEL.fields_by_name['name']._options = None
_GPIOMODULECHANNEL.fields_by_name['capabilities']._options = None
_GPIOMODULECHANNEL.fields_by_name['claimedBy']._options = None
_BLOCK.fields_by_name['channels']._options = None
_BLOCK.fields_by_name['modulePosition']._options = None
_BLOCK.fields_by_name['moduleStatus']._options = None
_BLOCK.fields_by_name['pullUpDesired']._options = None
_BLOCK.fields_by_name['pullUpStatus']._options = None
_BLOCK.fields_by_name['pullUpWhenActive']._options = None
_BLOCK.fields_by_name['pullUpWhenInactive']._options = None
_BLOCK.fields_by_name['pullDownDesired']._options = None
_BLOCK.fields_by_name['pullDownStatus']._options = None
_BLOCK.fields_by_name['pullDownWhenActive']._options = None
_BLOCK.fields_by_name['pullDownWhenInactive']._options = None
_BLOCK.fields_by_name['overCurrent']._options = None
_BLOCK.fields_by_name['openLoad']._options = None
_BLOCK.fields_by_name['moduleStatusClear']._options = None
_BLOCK._options = None
# @@protoc_insertion_point(module_scope)

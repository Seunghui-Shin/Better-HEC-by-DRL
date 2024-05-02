# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GripperConfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Common_pb2 as Common__pb2

from .Common_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='GripperConfig.proto',
  package='Kinova.Api.GripperConfig',
  syntax='proto3',
  serialized_pb=_b('\n\x13GripperConfig.proto\x12\x18Kinova.Api.GripperConfig\x1a\x0c\x43ommon.proto*\xb7\x02\n\x10SafetyIdentifier\x12*\n&UNSPECIFIED_ACTUATOR_SAFETY_IDENTIFIER\x10\x00\x12\x19\n\x15MAXIMUM_MOTOR_CURRENT\x10\x01\x12\x13\n\x0fMAXIMUM_VOLTAGE\x10\x02\x12\x13\n\x0fMINIMUM_VOLTAGE\x10\x04\x12\x1d\n\x19MAXIMUM_MOTOR_TEMPERATURE\x10\x08\x12\x1c\n\x18MAXIMUM_CORE_TEMPERATURE\x10\x10\x12!\n\x1dNON_VOLATILE_MEMORY_CORRUPTED\x10 \x12\x1b\n\x17\x45MERGENCY_LINE_ASSERTED\x10@\x12\x1c\n\x17\x43OMMUNICATION_TICK_LOST\x10\x80\x01\x12\x17\n\x12WATCHDOG_TRIGGERED\x10\x80\x02*\xb3\x01\n\x19RobotiqGripperStatusFlags\x12\x1e\n\x1aUNSPECIFIED_ROBOTIQ_STATUS\x10\x00\x12\x1c\n\x18ROBOTIQ_STAT_INITIALIZED\x10\x01\x12 \n\x1cROBOTIQ_STAT_OBJECT_DETECTED\x10\x02\x12\x1c\n\x18ROBOTIQ_STAT_POS_REACHED\x10\x04\x12\x18\n\x14ROBOTIQ_STAT_STOPPED\x10\x08P\x00\x62\x06proto3')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,],
  public_dependencies=[Common__pb2.DESCRIPTOR,])

_SAFETYIDENTIFIER = _descriptor.EnumDescriptor(
  name='SafetyIdentifier',
  full_name='Kinova.Api.GripperConfig.SafetyIdentifier',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_ACTUATOR_SAFETY_IDENTIFIER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMUM_MOTOR_CURRENT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMUM_VOLTAGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINIMUM_VOLTAGE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMUM_MOTOR_TEMPERATURE', index=4, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMUM_CORE_TEMPERATURE', index=5, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NON_VOLATILE_MEMORY_CORRUPTED', index=6, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMERGENCY_LINE_ASSERTED', index=7, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMUNICATION_TICK_LOST', index=8, number=128,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WATCHDOG_TRIGGERED', index=9, number=256,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=64,
  serialized_end=375,
)
_sym_db.RegisterEnumDescriptor(_SAFETYIDENTIFIER)

SafetyIdentifier = enum_type_wrapper.EnumTypeWrapper(_SAFETYIDENTIFIER)
_ROBOTIQGRIPPERSTATUSFLAGS = _descriptor.EnumDescriptor(
  name='RobotiqGripperStatusFlags',
  full_name='Kinova.Api.GripperConfig.RobotiqGripperStatusFlags',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_ROBOTIQ_STATUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOTIQ_STAT_INITIALIZED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOTIQ_STAT_OBJECT_DETECTED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOTIQ_STAT_POS_REACHED', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOTIQ_STAT_STOPPED', index=4, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=378,
  serialized_end=557,
)
_sym_db.RegisterEnumDescriptor(_ROBOTIQGRIPPERSTATUSFLAGS)

RobotiqGripperStatusFlags = enum_type_wrapper.EnumTypeWrapper(_ROBOTIQGRIPPERSTATUSFLAGS)
UNSPECIFIED_ACTUATOR_SAFETY_IDENTIFIER = 0
MAXIMUM_MOTOR_CURRENT = 1
MAXIMUM_VOLTAGE = 2
MINIMUM_VOLTAGE = 4
MAXIMUM_MOTOR_TEMPERATURE = 8
MAXIMUM_CORE_TEMPERATURE = 16
NON_VOLATILE_MEMORY_CORRUPTED = 32
EMERGENCY_LINE_ASSERTED = 64
COMMUNICATION_TICK_LOST = 128
WATCHDOG_TRIGGERED = 256
UNSPECIFIED_ROBOTIQ_STATUS = 0
ROBOTIQ_STAT_INITIALIZED = 1
ROBOTIQ_STAT_OBJECT_DETECTED = 2
ROBOTIQ_STAT_POS_REACHED = 4
ROBOTIQ_STAT_STOPPED = 8


DESCRIPTOR.enum_types_by_name['SafetyIdentifier'] = _SAFETYIDENTIFIER
DESCRIPTOR.enum_types_by_name['RobotiqGripperStatusFlags'] = _ROBOTIQGRIPPERSTATUSFLAGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
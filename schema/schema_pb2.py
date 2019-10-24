# -*- coding: utf-8 -*-
# source: schema/schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema/schema.proto',
  package='falco.schema',
  syntax='proto3',
  serialized_options=_b('Z1github.com/falcosecurity/client-go/pkg/api/schema'),
  serialized_pb=_b('\n\x13schema/schema.proto\x12\x0c\x66\x61lco.schema*\xcc\x02\n\x08priority\x12\r\n\tEMERGENCY\x10\x00\x12\r\n\temergency\x10\x00\x12\r\n\tEmergency\x10\x00\x12\t\n\x05\x41LERT\x10\x01\x12\t\n\x05\x61lert\x10\x01\x12\t\n\x05\x41lert\x10\x01\x12\x0c\n\x08\x43RITICAL\x10\x02\x12\x0c\n\x08\x63ritical\x10\x02\x12\x0c\n\x08\x43ritical\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\t\n\x05\x65rror\x10\x03\x12\t\n\x05\x45rror\x10\x03\x12\x0b\n\x07WARNING\x10\x04\x12\x0b\n\x07warning\x10\x04\x12\x0b\n\x07Warning\x10\x04\x12\n\n\x06NOTICE\x10\x05\x12\n\n\x06notice\x10\x05\x12\n\n\x06Notice\x10\x05\x12\x11\n\rINFORMATIONAL\x10\x06\x12\x11\n\rinformational\x10\x06\x12\x11\n\rInformational\x10\x06\x12\t\n\x05\x44\x45\x42UG\x10\x07\x12\t\n\x05\x64\x65\x62ug\x10\x07\x12\t\n\x05\x44\x65\x62ug\x10\x07\x1a\x02\x10\x01*o\n\x06source\x12\x0b\n\x07SYSCALL\x10\x00\x12\x0b\n\x07syscall\x10\x00\x12\x0b\n\x07Syscall\x10\x00\x12\r\n\tK8S_AUDIT\x10\x01\x12\r\n\tk8s_audit\x10\x01\x12\r\n\tK8s_audit\x10\x01\x12\r\n\tK8S_audit\x10\x01\x1a\x02\x10\x01\x42\x33Z1github.com/falcosecurity/client-go/pkg/api/schemab\x06proto3')
)

_PRIORITY = _descriptor.EnumDescriptor(
  name='priority',
  full_name='falco.schema.priority',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMERGENCY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='emergency', index=1, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Emergency', index=2, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALERT', index=3, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='alert', index=4, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Alert', index=5, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITICAL', index=6, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='critical', index=7, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Critical', index=8, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=9, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='error', index=10, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Error', index=11, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=12, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='warning', index=13, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Warning', index=14, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTICE', index=15, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='notice', index=16, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Notice', index=17, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFORMATIONAL', index=18, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='informational', index=19, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Informational', index=20, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=21, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='debug', index=22, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Debug', index=23, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=_b('\020\001'),
  serialized_start=38,
  serialized_end=370,
)
_sym_db.RegisterEnumDescriptor(_PRIORITY)

priority = enum_type_wrapper.EnumTypeWrapper(_PRIORITY)
_SOURCE = _descriptor.EnumDescriptor(
  name='source',
  full_name='falco.schema.source',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SYSCALL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='syscall', index=1, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Syscall', index=2, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='K8S_AUDIT', index=3, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k8s_audit', index=4, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='K8s_audit', index=5, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='K8S_audit', index=6, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=_b('\020\001'),
  serialized_start=372,
  serialized_end=483,
)
_sym_db.RegisterEnumDescriptor(_SOURCE)

source = enum_type_wrapper.EnumTypeWrapper(_SOURCE)
EMERGENCY = 0
emergency = 0
Emergency = 0
ALERT = 1
alert = 1
Alert = 1
CRITICAL = 2
critical = 2
Critical = 2
ERROR = 3
error = 3
Error = 3
WARNING = 4
warning = 4
Warning = 4
NOTICE = 5
notice = 5
Notice = 5
INFORMATIONAL = 6
informational = 6
Informational = 6
DEBUG = 7
debug = 7
Debug = 7
SYSCALL = 0
syscall = 0
Syscall = 0
K8S_AUDIT = 1
k8s_audit = 1
K8s_audit = 1
K8S_audit = 1


DESCRIPTOR.enum_types_by_name['priority'] = _PRIORITY
DESCRIPTOR.enum_types_by_name['source'] = _SOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
_PRIORITY._options = None
_SOURCE._options = None
# @@protoc_insertion_point(module_scope)

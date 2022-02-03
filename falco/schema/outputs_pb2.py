# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: outputs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import schema_pb2 as schema__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='outputs.proto',
  package='falco.outputs',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\routputs.proto\x12\rfalco.outputs\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0cschema.proto\"\t\n\x07request\"\xd8\x02\n\x08response\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x08priority\x18\x02 \x01(\x0e\x32\x16.falco.schema.priority\x12\x33\n\x11source_deprecated\x18\x03 \x01(\x0e\x32\x14.falco.schema.sourceB\x02\x18\x01\x12\x0c\n\x04rule\x18\x04 \x01(\t\x12\x0e\n\x06output\x18\x05 \x01(\t\x12@\n\routput_fields\x18\x06 \x03(\x0b\x32).falco.outputs.response.OutputFieldsEntry\x12\x10\n\x08hostname\x18\x07 \x01(\t\x12\x0c\n\x04tags\x18\x08 \x03(\t\x12\x0e\n\x06source\x18\t \x01(\t\x1a\x33\n\x11OutputFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x7f\n\x07service\x12:\n\x03sub\x12\x16.falco.outputs.request\x1a\x17.falco.outputs.response(\x01\x30\x01\x12\x38\n\x03get\x12\x16.falco.outputs.request\x1a\x17.falco.outputs.response0\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,schema__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='request',
  full_name='falco.outputs.request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=79,
  serialized_end=88,
)


_RESPONSE_OUTPUTFIELDSENTRY = _descriptor.Descriptor(
  name='OutputFieldsEntry',
  full_name='falco.outputs.response.OutputFieldsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='falco.outputs.response.OutputFieldsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='falco.outputs.response.OutputFieldsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=435,
)

_RESPONSE = _descriptor.Descriptor(
  name='response',
  full_name='falco.outputs.response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='falco.outputs.response.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='priority', full_name='falco.outputs.response.priority', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_deprecated', full_name='falco.outputs.response.source_deprecated', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rule', full_name='falco.outputs.response.rule', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output', full_name='falco.outputs.response.output', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_fields', full_name='falco.outputs.response.output_fields', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='falco.outputs.response.hostname', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='falco.outputs.response.tags', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='falco.outputs.response.source', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_OUTPUTFIELDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=435,
)

_RESPONSE_OUTPUTFIELDSENTRY.containing_type = _RESPONSE
_RESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RESPONSE.fields_by_name['priority'].enum_type = schema__pb2._PRIORITY
_RESPONSE.fields_by_name['source_deprecated'].enum_type = schema__pb2._SOURCE
_RESPONSE.fields_by_name['output_fields'].message_type = _RESPONSE_OUTPUTFIELDSENTRY
DESCRIPTOR.message_types_by_name['request'] = _REQUEST
DESCRIPTOR.message_types_by_name['response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

request = _reflection.GeneratedProtocolMessageType('request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'outputs_pb2'
  # @@protoc_insertion_point(class_scope:falco.outputs.request)
  })
_sym_db.RegisterMessage(request)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), {

  'OutputFieldsEntry' : _reflection.GeneratedProtocolMessageType('OutputFieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_OUTPUTFIELDSENTRY,
    '__module__' : 'outputs_pb2'
    # @@protoc_insertion_point(class_scope:falco.outputs.response.OutputFieldsEntry)
    })
  ,
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'outputs_pb2'
  # @@protoc_insertion_point(class_scope:falco.outputs.response)
  })
_sym_db.RegisterMessage(response)
_sym_db.RegisterMessage(response.OutputFieldsEntry)


_RESPONSE_OUTPUTFIELDSENTRY._options = None
_RESPONSE.fields_by_name['source_deprecated']._options = None

_SERVICE = _descriptor.ServiceDescriptor(
  name='service',
  full_name='falco.outputs.service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=437,
  serialized_end=564,
  methods=[
  _descriptor.MethodDescriptor(
    name='sub',
    full_name='falco.outputs.service.sub',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='falco.outputs.service.get',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICE)

DESCRIPTOR.services_by_name['service'] = _SERVICE

# @@protoc_insertion_point(module_scope)

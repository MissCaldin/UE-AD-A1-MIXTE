# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: showtime.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'showtime.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eshowtime.proto\"\x07\n\x05\x45mpty\"*\n\x0b\x41llSchedule\x12\x1b\n\x08schedule\x18\x01 \x03(\x0b\x32\t.Schedule\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"(\n\x08Schedule\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"\x15\n\x07MovieID\x12\n\n\x02id\x18\x01 \x01(\t\"-\n\rMovieSchedule\x12\r\n\x05movie\x18\x01 \x01(\t\x12\r\n\x05\x64\x61tes\x18\x02 \x03(\t2\x8a\x01\n\x08Showtime\x12%\n\x0bGetSchedule\x12\x06.Empty\x1a\x0c.AllSchedule\"\x00\x12\'\n\x11GetScheduleByDate\x12\x05.Date\x1a\t.Schedule\"\x00\x12.\n\x10GetMovieSchedule\x12\x08.MovieID\x1a\x0e.MovieSchedule\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'showtime_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=18
  _globals['_EMPTY']._serialized_end=25
  _globals['_ALLSCHEDULE']._serialized_start=27
  _globals['_ALLSCHEDULE']._serialized_end=69
  _globals['_DATE']._serialized_start=71
  _globals['_DATE']._serialized_end=91
  _globals['_SCHEDULE']._serialized_start=93
  _globals['_SCHEDULE']._serialized_end=133
  _globals['_MOVIEID']._serialized_start=135
  _globals['_MOVIEID']._serialized_end=156
  _globals['_MOVIESCHEDULE']._serialized_start=158
  _globals['_MOVIESCHEDULE']._serialized_end=203
  _globals['_SHOWTIME']._serialized_start=206
  _globals['_SHOWTIME']._serialized_end=344
# @@protoc_insertion_point(module_scope)

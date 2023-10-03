# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: similarity_search.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17similarity_search.proto\x12\nsimilarity\"\'\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"0\n\x0e\x41\x64\x64ItemRequest\x12\x1e\n\x04item\x18\x01 \x01(\x0b\x32\x10.similarity.Item\"3\n\x0f\x41\x64\x64ItemResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"#\n\x12SearchItemsRequest\x12\r\n\x05query\x18\x01 \x01(\t\"I\n\x0cSearchResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x18\n\x10similarity_score\x18\x03 \x01(\x02\"(\n\x13SearchItemsResponse\x12\x11\n\tsearch_id\x18\x01 \x01(\t\",\n\x17GetSearchResultsRequest\x12\x11\n\tsearch_id\x18\x01 \x01(\t\"E\n\x18GetSearchResultsResponse\x12)\n\x07results\x18\x01 \x03(\x0b\x32\x18.similarity.SearchResult2\x85\x02\n\x10SimilaritySearch\x12\x42\n\x07\x41\x64\x64Item\x12\x1a.similarity.AddItemRequest\x1a\x1b.similarity.AddItemResponse\x12N\n\x0bSearchItems\x12\x1e.similarity.SearchItemsRequest\x1a\x1f.similarity.SearchItemsResponse\x12]\n\x10GetSearchResults\x12#.similarity.GetSearchResultsRequest\x1a$.similarity.GetSearchResultsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'similarity_search_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ITEM']._serialized_start=39
  _globals['_ITEM']._serialized_end=78
  _globals['_ADDITEMREQUEST']._serialized_start=80
  _globals['_ADDITEMREQUEST']._serialized_end=128
  _globals['_ADDITEMRESPONSE']._serialized_start=130
  _globals['_ADDITEMRESPONSE']._serialized_end=181
  _globals['_SEARCHITEMSREQUEST']._serialized_start=183
  _globals['_SEARCHITEMSREQUEST']._serialized_end=218
  _globals['_SEARCHRESULT']._serialized_start=220
  _globals['_SEARCHRESULT']._serialized_end=293
  _globals['_SEARCHITEMSRESPONSE']._serialized_start=295
  _globals['_SEARCHITEMSRESPONSE']._serialized_end=335
  _globals['_GETSEARCHRESULTSREQUEST']._serialized_start=337
  _globals['_GETSEARCHRESULTSREQUEST']._serialized_end=381
  _globals['_GETSEARCHRESULTSRESPONSE']._serialized_start=383
  _globals['_GETSEARCHRESULTSRESPONSE']._serialized_end=452
  _globals['_SIMILARITYSEARCH']._serialized_start=455
  _globals['_SIMILARITYSEARCH']._serialized_end=716
# @@protoc_insertion_point(module_scope)

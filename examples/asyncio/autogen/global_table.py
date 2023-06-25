# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.

from __future__ import annotations
from typing import List, Iterator, Callable

from spacetimedb_python_sdk.spacetimedb_client import SpacetimeDBClient

class GlobalTable:
	is_table_class = True

	primary_key = "version"

	@classmethod
	def register_row_update(cls, callback: Callable[[str,GlobalTable,GlobalTable], None]):
		SpacetimeDBClient.instance._register_row_update("GlobalTable",callback)

	@classmethod
	def iter(cls) -> Iterator[GlobalTable]:
		return SpacetimeDBClient.instance._get_table_cache("GlobalTable").values()

	@classmethod
	def filter_by_version(cls, version) -> GlobalTable:
		return next(iter([column_value for column_value in SpacetimeDBClient.instance._get_table_cache("GlobalTable").values() if column_value.version == version]), None)

	@classmethod
	def filter_by_message_of_the_day(cls, message_of_the_day) -> List[GlobalTable]:
		return [column_value for column_value in SpacetimeDBClient.instance._get_table_cache("GlobalTable").values() if column_value.message_of_the_day == message_of_the_day]

	def __init__(self, data: List[object]):
		self.data = {}
		self.data["version"] = int(data[0])
		self.data["message_of_the_day"] = str(data[1])

	def encode(self) -> List[object]:
		return [self.version, self.message_of_the_day]

	def __getattr__(self, name: str):
		return self.data.get(name)

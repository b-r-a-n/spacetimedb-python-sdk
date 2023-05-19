# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.

from __future__ import annotations
from typing import List, Iterator, Callable

from spacetimedb_python_sdk.spacetimedb_client import SpacetimeDBClient
from .exit import Exit

class Room:
	is_table_class = True

	@classmethod
	def register_row_update(cls, callback: Callable[[str,Room,Room], None]):
		SpacetimeDBClient.instance._register_row_update("Room",callback)

	@classmethod
	def iter(cls) -> Iterator[Room]:
		return SpacetimeDBClient.instance._get_table_cache("Room").values()

	@classmethod
	def filter_by_room_id(cls, room_id) -> Room:
		return next(iter([column_value for column_value in SpacetimeDBClient.instance._get_table_cache("Room").values() if column_value.room_id == room_id]), None)

	@classmethod
	def filter_by_name(cls, name) -> List[Room]:
		return [column_value for column_value in SpacetimeDBClient.instance._get_table_cache("Room").values() if column_value.name == name]

	@classmethod
	def filter_by_description(cls, description) -> List[Room]:
		return [column_value for column_value in SpacetimeDBClient.instance._get_table_cache("Room").values() if column_value.description == description]

	def __init__(self, data: List[object]):
		self.data = {}
		self.data["room_id"] = str(data[0])
		self.data["name"] = str(data[1])
		self.data["description"] = str(data[2])
		self.data["exits"] = [Exit(item) for item in data[3]]
		self.data["spawnable_entities"] = [int(item) for item in data[4]]

	def encode(self) -> List[object]:
		return [self.room_id, self.name, self.description, self.exits, self.spawnable_entities]

	def __getattr__(self, name: str):
		return self.data.get(name)

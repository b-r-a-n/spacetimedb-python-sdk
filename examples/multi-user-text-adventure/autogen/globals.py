# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.

from __future__ import annotations
from typing import List, Iterator, Callable

from spacetimedb_python_sdk.spacetimedb_client import SpacetimeDBClient

class Globals:
	is_table_class = True

	@classmethod
	def register_row_update(cls, callback: Callable[[str,Globals,Globals], None]):
		SpacetimeDBClient.instance._register_row_update("Globals",callback)

	@classmethod
	def iter(cls) -> Iterator[Globals]:
		return SpacetimeDBClient.instance._get_table_cache("Globals").values()

	@classmethod
	def filter_by_id(cls, id) -> Globals:
		return next(iter([column_value for column_value in SpacetimeDBClient.instance._get_table_cache("Globals").values() if column_value.id == id]), None)

	@classmethod
	def filter_by_spawnable_entity_id_counter(cls, spawnable_entity_id_counter) -> List[Globals]:
		return [column_value for column_value in SpacetimeDBClient.instance._get_table_cache("Globals").values() if column_value.spawnable_entity_id_counter == spawnable_entity_id_counter]

	def __init__(self, data: List[object]):
		self.data = {}
		self.data["id"] = int(data[0])
		self.data["spawnable_entity_id_counter"] = int(data[1])

	def encode(self) -> List[object]:
		return [self.id, self.spawnable_entity_id_counter]

	def __getattr__(self, name: str):
		return self.data.get(name)

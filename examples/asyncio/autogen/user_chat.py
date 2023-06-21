# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.

from __future__ import annotations
from typing import List, Iterator, Callable

from spacetimedb_python_sdk.spacetimedb_client import SpacetimeDBClient

class UserChat:
	is_table_class = True

	@classmethod
	def register_row_update(cls, callback: Callable[[str,UserChat,UserChat], None]):
		SpacetimeDBClient.instance._register_row_update("UserChat",callback)

	@classmethod
	def iter(cls) -> Iterator[UserChat]:
		return SpacetimeDBClient.instance._get_table_cache("UserChat").values()

	@classmethod
	def filter_by_chat_entity_id(cls, chat_entity_id) -> List[UserChat]:
		return [column_value for column_value in SpacetimeDBClient.instance._get_table_cache("UserChat").values() if column_value.chat_entity_id == chat_entity_id]

	@classmethod
	def filter_by_owner_id(cls, owner_id) -> List[UserChat]:
		return [column_value for column_value in SpacetimeDBClient.instance._get_table_cache("UserChat").values() if column_value.owner_id == owner_id]

	@classmethod
	def filter_by_chat(cls, chat) -> List[UserChat]:
		return [column_value for column_value in SpacetimeDBClient.instance._get_table_cache("UserChat").values() if column_value.chat == chat]

	def __init__(self, data: List[object]):
		self.data = {}
		self.data["chat_entity_id"] = int(data[0])
		self.data["owner_id"] = bytes.fromhex(data[1])
		self.data["chat"] = str(data[2])

	def encode(self) -> List[object]:
		return [self.chat_entity_id, self.owner_id, self.chat]

	def __getattr__(self, name: str):
		return self.data.get(name)

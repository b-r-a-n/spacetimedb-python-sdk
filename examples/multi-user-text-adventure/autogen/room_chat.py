# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.

from __future__ import annotations
from typing import List, Iterator, Callable

from spacetimedb_sdk.spacetimedb_client import SpacetimeDBClient


class RoomChat:
    is_table_class = True

    primary_key = "chat_entity_id"

    @classmethod
    def register_row_update(cls, callback: Callable[[str, RoomChat, RoomChat], None]):
        SpacetimeDBClient.instance._register_row_update("RoomChat", callback)

    @classmethod
    def iter(cls) -> Iterator[RoomChat]:
        return SpacetimeDBClient.instance._get_table_cache("RoomChat").values()

    @classmethod
    def filter_by_chat_entity_id(cls, chat_entity_id) -> RoomChat:
        return next(
            iter(
                [
                    column_value
                    for column_value in SpacetimeDBClient.instance._get_table_cache(
                        "RoomChat"
                    ).values()
                    if column_value.chat_entity_id == chat_entity_id
                ]
            ),
            None,
        )

    @classmethod
    def filter_by_room_id(cls, room_id) -> List[RoomChat]:
        return [
            column_value
            for column_value in SpacetimeDBClient.instance._get_table_cache(
                "RoomChat"
            ).values()
            if column_value.room_id == room_id
        ]

    @classmethod
    def filter_by_source_spawnable_entity_id(
        cls, source_spawnable_entity_id
    ) -> List[RoomChat]:
        return [
            column_value
            for column_value in SpacetimeDBClient.instance._get_table_cache(
                "RoomChat"
            ).values()
            if column_value.source_spawnable_entity_id == source_spawnable_entity_id
        ]

    @classmethod
    def filter_by_chat_text(cls, chat_text) -> List[RoomChat]:
        return [
            column_value
            for column_value in SpacetimeDBClient.instance._get_table_cache(
                "RoomChat"
            ).values()
            if column_value.chat_text == chat_text
        ]

    @classmethod
    def filter_by_timestamp(cls, timestamp) -> List[RoomChat]:
        return [
            column_value
            for column_value in SpacetimeDBClient.instance._get_table_cache(
                "RoomChat"
            ).values()
            if column_value.timestamp == timestamp
        ]

    def __init__(self, data: List[object]):
        self.data = {}
        self.data["chat_entity_id"] = int(data[0])
        self.data["room_id"] = str(data[1])
        self.data["source_spawnable_entity_id"] = int(data[2])
        self.data["chat_text"] = str(data[3])
        self.data["timestamp"] = int(data[4])

    def encode(self) -> List[object]:
        return [
            self.chat_entity_id,
            self.room_id,
            self.source_spawnable_entity_id,
            self.chat_text,
            self.timestamp,
        ]

    def __getattr__(self, name: str):
        return self.data.get(name)

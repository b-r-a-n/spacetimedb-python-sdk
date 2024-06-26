# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.

from typing import List, Callable, Optional

from spacetimedb_sdk.spacetimedb_client import SpacetimeDBClient
from spacetimedb_sdk.spacetimedb_client import Identity
from spacetimedb_sdk.spacetimedb_client import Address

from .point import Point

reducer_name = "create_player"

def create_player(name: str, location: Point):
	name = name
	location = location.encode()
	SpacetimeDBClient.instance._reducer_call("create_player", name, location)

def register_on_create_player(callback: Callable[[Identity, Optional[Address], str, str, str, Point], None]):
	SpacetimeDBClient.instance._register_reducer("create_player", callback)

def _decode_args(data):
	return [str(data[0]), Point(data[1])]

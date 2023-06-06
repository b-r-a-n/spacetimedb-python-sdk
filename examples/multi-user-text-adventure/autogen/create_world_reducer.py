# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.

from typing import List, Callable

from spacetimedb_python_sdk.spacetimedb_client import SpacetimeDBClient


def create_world(world_id: str, world_name: str, world_description: str):
	world_id = world_id
	world_name = world_name
	world_description = world_description
	SpacetimeDBClient.instance._reducer_call("create_world", world_id, world_name, world_description)

def register_on_create_world(callback: Callable[[bytes, str, str, str, str, str], None]):
	if not _check_callback_signature(callback):
		raise ValueError("Callback signature does not match expected arguments")

	SpacetimeDBClient.instance._register_reducer("create_world", callback)

def _decode_args(data):
	return [str(data[0]), str(data[1]), str(data[2])]

def _check_callback_signature(callback: Callable) -> bool:
	expected_arguments = [bytes, str, str, str, str, str]
	callback_arguments = callback.__annotations__.values()

	return list(callback_arguments) == expected_arguments

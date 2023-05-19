# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.

from typing import List, Callable

from spacetimedb_python_sdk.spacetimedb_client import SpacetimeDBClient


def user_chat(chat: str):
	chat = chat
	SpacetimeDBClient.instance._reducer_call("user_chat", chat)

def register_on_user_chat(callback: Callable[[bytes, str, str, str], None]):
	if not _check_callback_signature(callback):
		raise ValueError("Callback signature does not match expected arguments")

	SpacetimeDBClient.instance._register_reducer("user_chat", callback)

def _decode_args(data):
	return [str(data[0])]

def _check_callback_signature(callback: Callable) -> bool:
	expected_arguments = [bytes, str, str, str]
	callback_arguments = callback.__annotations__.values()

	return list(callback_arguments) == expected_arguments

# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.


class RoomChat:
	is_table_class = True

	def __init__(self, data):
		self.data = {}
		self.data["room_id"] = str(data[0])
		self.data["source_spawnable_entity_id"] = int(data[1])
		self.data["chat_text"] = str(data[2])

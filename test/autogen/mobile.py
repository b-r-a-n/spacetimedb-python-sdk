# THIS FILE IS AUTOMATICALLY GENERATED BY SPACETIMEDB. EDITS TO THIS FILE
# WILL NOT BE SAVED. MODIFY TABLES IN RUST INSTEAD.


class Mobile:
	is_table_class = True

	def __init__(self, data):
		self.data = {}
		self.data["name"] = str(data[0])
		self.data["description"] = str(data[1])

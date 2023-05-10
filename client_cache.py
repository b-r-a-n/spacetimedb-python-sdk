import importlib
import pkgutil


class TableCache:
    def __init__(self, table_class):
        self.entries = {}
        self.table_class = table_class

    def decode(self, value):
        return self.table_class(value)

    def set_entry(self, key, value):
        self.entries[key] = self.decode(value)

    def set_entry_decoded(self, key, decoded_value):
        self.entries[key] = decoded_value

    def delete_entry(self, key):
        if key in self.entries:
            del self.entries[key]


class ClientCache:
    _instance = None

    @classmethod
    def get_instance(cls):
        if ClientCache._instance is None:
            ClientCache()
        return ClientCache._instance

    @classmethod
    def get_table_dict(cls, table_name):
        return ClientCache.get_instance().tables[table_name].entries

    def __init__(self, autogen_package):
        self.tables = {}

        for importer, module_name, is_package in pkgutil.iter_modules(autogen_package.__path__):
            if not is_package:
                module = importlib.import_module(
                    f"{autogen_package.__name__}.{module_name}")

                # Assuming table class name is the same as the module name
                table_class_name = module_name.capitalize()

                if hasattr(module, table_class_name):
                    table_class = getattr(module, table_class_name)

                    # Check for a special property, e.g. 'is_table_class'
                    if getattr(table_class, 'is_table_class', False):
                        self.tables[table_class_name] = TableCache(table_class)

    def decode(self, table_name, value):
        if not table_name in self.tables:
            print("Error, table not found.")
            return

        return self.tables[table_name].decode(value)

    def set_entry(self, table_name, key, value):
        if not table_name in self.tables:
            print("Error, table not found.")
            return

        self.tables[table_name].set_entry(key, value)

    def set_entry_decoded(self, table_name, key, value):
        if not table_name in self.tables:
            print("Error, table not found.")
            return

        self.tables[table_name].set_entry_decoded(key, value)

    def delete_entry(self, table_name, key, value):
        if not table_name in self.tables:
            print("Error, table not found.")
            return

        self.tables[table_name].delete_entry(key, value)

    def get_entry(self, table_name, key):
        return self.tables[table_name].entries[key]

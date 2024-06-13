import unittest
from unittest.mock import patch

import module_bindings

from spacetimedb_sdk.spacetimedb_client import SpacetimeDBClient

class TestSpacetimeDBClient(unittest.TestCase):

    @patch('spacetimedb_sdk.spacetime_websocket_client.WebSocketClient')
    def test_subscribe(self, MockWebsocketClient):
        client = SpacetimeDBClient(module_bindings)
        client.wsc = MockWebsocketClient()
        client.subscribe(["SELECT * FROM Position", "SELECT * FROM Coin"])
        client.wsc.send.assert_called_with(b'{"subscribe": { "query_strings": ["SELECT * FROM Position", "SELECT * FROM Coin"]}}')

if __name__ == '__main__':
    unittest.main()
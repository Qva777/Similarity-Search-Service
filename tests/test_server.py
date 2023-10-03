from unittest.mock import MagicMock
import unittest

import similarity_search_pb2
from server import SimilaritySearchServicer


class TestSimilaritySearchServicer(unittest.TestCase):

    def test_AddItem(self):
        # Create a mock for the database connection
        mock_conn = MagicMock()

        # Initialize the servicer with the mock connection
        servicer = SimilaritySearchServicer()
        servicer.conn = mock_conn

        # Create a mock request with item details
        item_id = "item1"
        item_description = "This is item 1."
        request = similarity_search_pb2.AddItemRequest(item=similarity_search_pb2.Item(id=item_id,
                                                                                       description=item_description))

        # Mock the database cursor
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # Mock the database query result to simulate an item with the given ID already existing
        mock_cursor.fetchone.return_value = (item_id,)

        # Call the AddItem method
        response = servicer.AddItem(request, None)

        # Assert the response
        self.assertFalse(response.success)
        self.assertEqual(response.message, f"Item with ID '{item_id}' already exists.")

        # Verify that the cursor executed the correct SQL statement to check for the existing item
        mock_cursor.execute.assert_called_once_with("SELECT item_id FROM items WHERE item_id=%s;", (item_id,))

        # Verify that the connection did not commit any transaction
        mock_conn.commit.assert_not_called()

    def test_SearchItems(self):
        # Create a mock for the database connection
        mock_conn = MagicMock()

        # Initialize the servicer with the mock connection
        servicer = SimilaritySearchServicer()
        servicer.conn = mock_conn

        # Create a mock request with a query
        query = "item"
        request = similarity_search_pb2.SearchItemsRequest(query=query)

        # Mock the database cursor
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        # Mock the database query result to simulate multiple items in the database
        mock_cursor.fetchall.return_value = [("item1", "This is item 1."), ("item2", "This is item 2.")]

        # Call the SearchItems method
        response = servicer.SearchItems(request, None)

        # Assert the response contains the correct search ID
        self.assertTrue(response.search_id.startswith("search_"))

        # Verify that the cursor executed the correct SQL statement to retrieve items from the database
        mock_cursor.execute.assert_called_once_with("SELECT item_id, description FROM items;")


if __name__ == "__main__":
    unittest.main()

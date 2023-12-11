"""
Module: test_app.py

This module contains unit tests for the Flask application in app.py.
"""

import unittest
from app import app

class TestApp(unittest.TestCase):
    """
    Test cases for the Flask application in app.py.
    """

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        """
        Test the '/hello' route.

        This test checks if the '/hello' route returns a status code of 200
        and the expected 'Hello, World!' message.
        """

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World From Beshlawy!')

if __name__ == '__main__':
    unittest.main()

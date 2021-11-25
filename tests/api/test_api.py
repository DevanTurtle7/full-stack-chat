"""
A testing module for the API

author: Devan Kavalchek
"""
import unittest
from server.api.db_utils import *
from server.server import rebuild_tables
from tests.test_utils import *

API_URL = "http://127.0.0.1:5000"

class TestApi(unittest.TestCase):
    def setUp(self):
        rebuild_tables()
        insert_test_data()
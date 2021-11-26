"""
A testing module for the API

author: Devan Kavalchek
"""
import unittest
from server.utils.db_utils import *
from server.server import rebuild_tables
from tests.utils.test_utils import *

API_URL = "http://127.0.0.1:5000"

class TestApi(unittest.TestCase):
    def setUp(self):
        rebuild_tables()
        insert_test_data()
    
    def test_get_chats(self):
        expected_num = 4
        expected_chat_1 = {'id': 2, 'name': 'ANOTHER CHAT', 'last_message': 'helloooo', 'last_sent': '2020-10-03T00:00:01'}
        expected_chat_2 = {'id': 2, 'name': 'Bob', 'last_message': 'Just testing out this app', 'last_sent': '1923-09-03T00:00:01'}
        expected_chat_3 = {'id': 1, 'name': 'OUR CHAT', 'last_message': 'hey whats up, welcome to the chat', 'last_sent': '1919-10-03T00:00:01'}
        expected_chat_4 = {'id': 3, 'name': 'james', 'last_message': 'hello', 'last_sent': '1921-10-03T00:00:01'}

        chats = get_rest_call(self, API_URL + "/chats", params={'user_id': 1})
        print(chats)

        self.assertEqual(expected_num, len(chats))
        self.assertEqual(chats[0], expected_chat_1)
        self.assertEqual(chats[1], expected_chat_2)
        self.assertEqual(chats[2], expected_chat_3)
        self.assertEqual(chats[3], expected_chat_4)

    def test_get_chats_no_id(self):
        expected = {"status": 400, "error": "Error, no user id provided"}
        actual = get_rest_call(self, API_URL + "/chats")

        self.assertEqual(expected, actual)
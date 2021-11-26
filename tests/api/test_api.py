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
    
    def test_get_chats_user_1(self):
        expected_num = 4
        expected_chat_1 = {'type': 'group_chat', 'id': 2, 'name': 'ANOTHER CHAT', 'last_message': 'helloooo', 'last_sent': '2020-10-03T00:00:01'}
        expected_chat_2 = {'type': 'direct_message', 'id': 2, 'name': 'Bob', 'last_message': 'Just testing out this app', 'last_sent': '1923-09-03T00:00:01'}
        expected_chat_3 = {'type': 'direct_message', 'id': 3, 'name': 'james', 'last_message': 'hello', 'last_sent': '1921-10-03T00:00:01'}
        expected_chat_4 = {'type': 'group_chat', 'id': 1, 'name': 'OUR CHAT', 'last_message': 'hey whats up, welcome to the chat', 'last_sent': '1919-10-03T00:00:01'}

        chats = get_rest_call(self, API_URL + "/chats", params={'user_id': 1})

        self.assertEqual(expected_num, len(chats))
        self.assertEqual(chats[0], expected_chat_1)
        self.assertEqual(chats[1], expected_chat_2)
        self.assertEqual(chats[2], expected_chat_3)
        self.assertEqual(chats[3], expected_chat_4)

    def test_get_chats_user_2(self):
        expected_num = 4
        expected_chat_1 = {'type': 'group_chat', 'id': 2, 'name': 'ANOTHER CHAT', 'last_message': 'helloooo', 'last_sent': '2020-10-03T00:00:01'}
        expected_chat_2 = {'type': 'direct_message', 'id': 1, 'name': 'devan', 'last_message': 'Just testing out this app', 'last_sent': '1923-09-03T00:00:01'}
        expected_chat_3 = {'type': 'direct_message', 'id': 3, 'name': 'james', 'last_message': 'dont talk to me', 'last_sent': '1920-10-04T00:00:01'}
        expected_chat_4 = {'type': 'group_chat', 'id': 1, 'name': 'OUR CHAT', 'last_message': 'hey whats up, welcome to the chat', 'last_sent': '1919-10-03T00:00:01'}

        chats = get_rest_call(self, API_URL + "/chats", params={'user_id': 2})

        self.assertEqual(expected_num, len(chats))
        self.assertEqual(chats[0], expected_chat_1)
        self.assertEqual(chats[1], expected_chat_2)
        self.assertEqual(chats[2], expected_chat_3)
        self.assertEqual(chats[3], expected_chat_4)

    def test_get_chats_user_3(self):
        expected_num = 4
        expected_chat_1 = {'type': 'group_chat', 'id': 2, 'name': 'ANOTHER CHAT', 'last_message': 'helloooo', 'last_sent': '2020-10-03T00:00:01'}
        expected_chat_2 = {'type': 'direct_message', 'id': 1, 'name': 'devan', 'last_message': 'hello', 'last_sent': '1921-10-03T00:00:01'}
        expected_chat_3 = {'type': 'direct_message', 'id': 2, 'name': 'Bob', 'last_message': 'dont talk to me', 'last_sent': '1920-10-04T00:00:01'}
        expected_chat_4 = {'type': 'group_chat', 'id': 1, 'name': 'OUR CHAT', 'last_message': 'hey whats up, welcome to the chat', 'last_sent': '1919-10-03T00:00:01'}

        chats = get_rest_call(self, API_URL + "/chats", params={'user_id': 3})

        self.assertEqual(expected_num, len(chats))
        self.assertEqual(chats[0], expected_chat_1)
        self.assertEqual(chats[1], expected_chat_2)
        self.assertEqual(chats[2], expected_chat_3)
        self.assertEqual(chats[3], expected_chat_4)

    def test_get_chats_user_4(self):
        expected_num = 1
        expected_chat = {'type': 'group_chat', 'id': 2, 'name': 'ANOTHER CHAT', 'last_message': 'helloooo', 'last_sent': '2020-10-03T00:00:01'}

        chats = get_rest_call(self, API_URL + "/chats", params={'user_id': 4})

        self.assertEqual(expected_num, len(chats))
        self.assertEqual(chats[0], expected_chat)

    def test_get_chats_no_id(self):
        expected = {"status": 400, "error": "Error, no user id provided"}
        actual = get_rest_call(self, API_URL + "/chats")

        self.assertEqual(expected, actual)
    
    def test_get_direct_messages_user_1_user_2(self):
        expected_num = 5
        expected_message_1 = {'id': 6, 'sender_id': 2, 'receiver_id': 1, 'message_text': 'ya same', 'time_sent': '1923-10-04T00:00:01', 'read': False}
        expected_message_2 = {'id': 4, 'sender_id': 1, 'receiver_id': 2, 'message_text': 'Just testing out this app', 'time_sent': '1923-09-03T00:00:01', 'read': False}
        expected_message_3 = {'id': 3, 'sender_id': 1, 'receiver_id': 2, 'message_text': 'Nothing much', 'time_sent': '1922-10-04T00:00:01', 'read': False}
        expected_message_4 = {'id': 2, 'sender_id': 2, 'receiver_id': 1, 'message_text': 'Oh hey, whats up?', 'time_sent': '1922-10-03T00:00:03', 'read': False}
        expected_message_5 = {'id': 1, 'sender_id': 1, 'receiver_id': 2, 'message_text': 'This is my first message', 'time_sent': '1922-10-03T00:00:01', 'read': False}

        messages = get_rest_call(self, API_URL + "/direct_messages", params={'user_id': 1, 'receiver_id': 2})

        self.assertEqual(expected_num, len(messages))
        self.assertEqual(messages[0], expected_message_1)
        self.assertEqual(messages[1], expected_message_2)
        self.assertEqual(messages[2], expected_message_3)
        self.assertEqual(messages[3], expected_message_4)
        self.assertEqual(messages[4], expected_message_5)
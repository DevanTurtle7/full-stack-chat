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
        expected_chat_2 = {'type': 'direct_message', 'id': 2, 'name': 'Bob', 'last_message': 'ya same', 'last_sent': '1923-10-04T00:00:01'}
        expected_chat_3 = {'type': 'group_chat', 'id': 1, 'name': 'OUR CHAT', 'last_message': 'pretty good pretty good', 'last_sent': '1923-10-03T00:00:01'}
        expected_chat_4 = {'type': 'direct_message', 'id': 3, 'name': 'james', 'last_message': 'yoyoyoy', 'last_sent': '1923-10-03T00:00:01'}

        chats = get_rest_call(self, API_URL + "/chats", params={'user_id': 1})

        self.assertEqual(expected_num, len(chats))
        self.assertEqual(chats[0], expected_chat_1)
        self.assertEqual(chats[1], expected_chat_2)
        self.assertEqual(chats[2], expected_chat_3)
        self.assertEqual(chats[3], expected_chat_4)

    def test_get_chats_user_2(self):
        expected_num = 4
        expected_chat_1 = {'type': 'group_chat', 'id': 2, 'name': 'ANOTHER CHAT', 'last_message': 'helloooo', 'last_sent': '2020-10-03T00:00:01'}
        expected_chat_2 = {'type': 'direct_message', 'id': 1, 'name': 'devan', 'last_message': 'ya same', 'last_sent': '1923-10-04T00:00:01'}
        expected_chat_3 = {'type': 'group_chat', 'id': 1, 'name': 'OUR CHAT', 'last_message': 'pretty good pretty good', 'last_sent': '1923-10-03T00:00:01'}
        expected_chat_4 = {'type': 'direct_message', 'id': 3, 'name': 'james', 'last_message': 'dont talk to me', 'last_sent': '1920-10-04T00:00:01'}

        chats = get_rest_call(self, API_URL + "/chats", params={'user_id': 2})

        self.assertEqual(expected_num, len(chats))
        self.assertEqual(chats[0], expected_chat_1)
        self.assertEqual(chats[1], expected_chat_2)
        self.assertEqual(chats[2], expected_chat_3)
        self.assertEqual(chats[3], expected_chat_4)

    def test_get_chats_user_3(self):
        expected_num = 4
        expected_chat_1 = {'type': 'group_chat', 'id': 2, 'name': 'ANOTHER CHAT', 'last_message': 'helloooo', 'last_sent': '2020-10-03T00:00:01'}
        expected_chat_2 = {'type': 'group_chat', 'id': 1, 'name': 'OUR CHAT', 'last_message': 'pretty good pretty good', 'last_sent': '1923-10-03T00:00:01'}
        expected_chat_3 = {'type': 'direct_message', 'id': 1, 'name': 'devan', 'last_message': 'yoyoyoy', 'last_sent': '1923-10-03T00:00:01'}
        expected_chat_4 = {'type': 'direct_message', 'id': 2, 'name': 'Bob', 'last_message': 'dont talk to me', 'last_sent': '1920-10-04T00:00:01'}

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
        expected_message_1 = {'sender_id': 2, 'receiver_id': 1, 'other_name': 'Bob', 'other_username': 'bob27', 'message_text': 'ya same', 'time_sent': '1923-10-04T00:00:01', 'read': False}
        expected_message_2 = {'sender_id': 1, 'receiver_id': 2, 'other_name': 'Bob', 'other_username': 'bob27', 'message_text': 'Just testing out this app', 'time_sent': '1923-09-03T00:00:01', 'read': False}
        expected_message_3 = {'sender_id': 1, 'receiver_id': 2, 'other_name': 'Bob', 'other_username': 'bob27', 'message_text': 'Nothing much', 'time_sent': '1922-10-04T00:00:01', 'read': False}
        expected_message_4 = {'sender_id': 2, 'receiver_id': 1, 'other_name': 'Bob', 'other_username': 'bob27', 'message_text': 'Oh hey, whats up?', 'time_sent': '1922-10-03T00:00:03', 'read': False}
        expected_message_5 = {'sender_id': 1, 'receiver_id': 2, 'other_name': 'Bob', 'other_username': 'bob27', 'message_text': 'This is my first message', 'time_sent': '1922-10-03T00:00:01', 'read': False}

        messages = get_rest_call(self, API_URL + "/direct_messages", params={'user_id': 1, 'receiver_id': 2})

        self.assertEqual(expected_num, len(messages))
        self.assertEqual(messages[0], expected_message_1)
        self.assertEqual(messages[1], expected_message_2)
        self.assertEqual(messages[2], expected_message_3)
        self.assertEqual(messages[3], expected_message_4)
        self.assertEqual(messages[4], expected_message_5)

    def test_get_direct_messages_user_1_user_2_limit(self):
        expected_num = 2
        expected_message_1 = {'sender_id': 2, 'receiver_id': 1, 'other_name': 'Bob', 'other_username': 'bob27', 'message_text': 'ya same', 'time_sent': '1923-10-04T00:00:01', 'read': False}
        expected_message_2 = {'sender_id': 1, 'receiver_id': 2, 'other_name': 'Bob', 'other_username': 'bob27', 'message_text': 'Just testing out this app', 'time_sent': '1923-09-03T00:00:01', 'read': False}

        messages = get_rest_call(self, API_URL + "/direct_messages", params={'user_id': 1, 'receiver_id': 2, 'limit': 2})

        self.assertEqual(expected_num, len(messages))
        self.assertEqual(messages[0], expected_message_1)
        self.assertEqual(messages[1], expected_message_2)
    
    def test_get_group_messages_user_1_chat_1(self):
        expected_num = 4
        expected_message_1 = {'sender_id': 2, 'sender_name': 'Bob', 'sender_username': 'bob27', 'group_chat_id': 1, 'group_chat_name': 'OUR CHAT', 'message_text': 'pretty good pretty good', 'time_sent': '1923-10-03T00:00:01', 'read': False}
        expected_message_2 = {'sender_id': 1, 'sender_name': 'devan', 'sender_username': 'dev', 'group_chat_id': 1, 'group_chat_name': 'OUR CHAT', 'message_text': 'hows it going?', 'time_sent': '1922-10-03T00:00:01', 'read': False}
        expected_message_3 = {'sender_id': 3, 'sender_name': 'james', 'sender_username': 'james2285', 'group_chat_id': 1, 'group_chat_name': 'OUR CHAT', 'message_text': 'yo whats up', 'time_sent': '1921-10-03T00:00:01', 'read': False}
        expected_message_4 = {'sender_id': 1, 'sender_name': 'devan', 'sender_username': 'dev', 'group_chat_id': 1, 'group_chat_name': 'OUR CHAT', 'message_text': 'hey whats up, welcome to the chat', 'time_sent': '1919-10-03T00:00:01', 'read': False}

        messages = get_rest_call(self, API_URL + "/group_messages", params={'user_id': 1, 'group_chat_id': 1})

        self.assertEqual(expected_num, len(messages))
        self.assertEqual(messages[0], expected_message_1)
        self.assertEqual(messages[1], expected_message_2)
        self.assertEqual(messages[2], expected_message_3)
        self.assertEqual(messages[3], expected_message_4)

    def test_get_group_messages_user_1_chat_1_limit(self):
        expected_num = 3
        expected_message_1 = {'sender_id': 2, 'sender_name': 'Bob', 'sender_username': 'bob27', 'group_chat_id': 1, 'group_chat_name': 'OUR CHAT', 'message_text': 'pretty good pretty good', 'time_sent': '1923-10-03T00:00:01', 'read': False}
        expected_message_2 = {'sender_id': 1, 'sender_name': 'devan', 'sender_username': 'dev', 'group_chat_id': 1, 'group_chat_name': 'OUR CHAT', 'message_text': 'hows it going?', 'time_sent': '1922-10-03T00:00:01', 'read': False}
        expected_message_3 = {'sender_id': 3, 'sender_name': 'james', 'sender_username': 'james2285', 'group_chat_id': 1, 'group_chat_name': 'OUR CHAT', 'message_text': 'yo whats up', 'time_sent': '1921-10-03T00:00:01', 'read': False}

        messages = get_rest_call(self, API_URL + "/group_messages", params={'user_id': 1, 'group_chat_id': 1, 'limit': 3})

        self.assertEqual(expected_num, len(messages))
        self.assertEqual(messages[0], expected_message_1)
        self.assertEqual(messages[1], expected_message_2)
        self.assertEqual(messages[2], expected_message_3)
    
    def test_send_direct_message(self):
        expected_num = 6
        expected_message = {'sender_id': 1, 'receiver_id': 2, 'other_name': 'Bob', 'other_username': 'bob27', 'message_text': 'This is a test of sending a message', 'time_sent': '2021-11-26T23:22:22.548075', 'read': False}

        post_rest_call(self, API_URL + "/direct_messages", params={'user_id': 1, 'receiver_id': 2, 'text': 'This is a test of sending a message'})
        messages = get_rest_call(self, API_URL + "/direct_messages", params={'user_id': 1, 'receiver_id': 2})
        message = messages[0]

        self.assertEqual(expected_num, len(messages))
        self.assertEqual(expected_message['sender_id'], message['sender_id'])
        self.assertEqual(expected_message['receiver_id'], message['receiver_id'])
        self.assertEqual(expected_message['other_name'], message['other_name'])
        self.assertEqual(expected_message['other_username'], message['other_username'])
        self.assertEqual(expected_message['message_text'], message['message_text'])
        self.assertEqual(expected_message['read'], message['read'])
    
    def test_send_group_message(self):
        expected_num = 5
        expected_message = {'sender_id': 1, 'sender_name': 'devan', 'sender_username': 'dev', 'group_chat_id': 1, 'group_chat_name': 'OUR CHAT', 'message_text': 'This is a test of sending a group message', 'time_sent': '2021-11-26T23:29:10.296296', 'read': False}

        post_rest_call(self, API_URL + "/group_messages", params={'user_id': 1, 'group_chat_id': 1, 'text': 'This is a test of sending a group message'})
        messages = get_rest_call(self, API_URL + "/group_messages", params={'user_id': 1, 'group_chat_id': 1})
        message = messages[0]

        self.assertEqual(expected_num, len(messages))
        self.assertEqual(expected_message['sender_id'], message['sender_id'])
        self.assertEqual(expected_message['sender_name'], message['sender_name'])
        self.assertEqual(expected_message['sender_username'], message['sender_username'])
        self.assertEqual(expected_message['group_chat_id'], message['group_chat_id'])
        self.assertEqual(expected_message['group_chat_name'], message['group_chat_name'])
        self.assertEqual(expected_message['message_text'], message['message_text'])
        self.assertEqual(expected_message['read'], message['read'])
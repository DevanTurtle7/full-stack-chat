from flask_restful import Resource
from flask_restful import request
from flask_restful import reqparse
import json
from datetime import datetime, date

# For testing/production
try:
    from server.utils.db_utils import *
    from server.utils.jsonify import jsonify_sql
except:
    from utils.db_utils import *
    from utils.jsonify import jsonify_sql

class GroupMessages(Resource):
    def __init__(self):
        self.__columns = ["sender_id", "sender_name", "sender_username", "group_chat_id", "group_chat_name", "message_text", "time_sent", "read"]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        parser.add_argument("group_chat_id", type=int)
        parser.add_argument("limit", type=int)
        args = parser.parse_args()

        user_id = args["user_id"]
        group_chat_id = args["group_chat_id"]
        limit = args["limit"]

        if user_id != None and group_chat_id != None:
            user_id = int(user_id)
            group_chat_id = int(group_chat_id)

            sql_string = """
                SELECT sender_id, users.name as sender_name, users.username as sender_username,
                group_messages.group_chat_id, group_chats.name as grop_chat_name, message_text,
                time_sent, read
                FROM group_messages INNER JOIN group_chats ON group_messages.group_chat_id = group_chats.id
                INNER JOIN group_memberships ON group_memberships.group_chat_id = group_chats.id
                INNER JOIN users ON group_messages.sender_id = users.id
                WHERE group_memberships.user_id = %(user_id)s AND group_messages.group_chat_id = %(group_chat_id)s
                ORDER BY time_sent DESC
            """

            args = {'user_id': user_id, 'group_chat_id': group_chat_id}

            if limit != None:
                limit = int(limit)
                sql_string += " LIMIT %(limit)s"
                args['limit'] = limit

            sql_data = exec_get_all(sql_string, args)
            result = jsonify_sql(sql_data, self.__columns)
            print(result)

            return result
        else:
            return {"status": 400, "error": "Error, no user id or group chat id provided"}
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        parser.add_argument("group_chat_id", type=int)
        parser.add_argument("text", type=str)
        args = parser.parse_args()

        user_id = args["user_id"]
        group_chat_id = args["group_chat_id"]
        text = args["text"]

        if user_id != None and group_chat_id != None and text != None:
            user_id = int(user_id)
            group_chat_id = int(group_chat_id)
            text = str(text)

            sql_string = """
                INSERT INTO group_messages(sender_id, group_chat_id, message_text) VALUES
                (%(user_id)s, %(group_chat_id)s, %(message_text)s)
            """
            args = {'user_id': user_id, 'group_chat_id': group_chat_id, 'message_text': text}

            exec_commit(sql_string, args)

            return {"status": 201, "success": "Message was sent successfully"}
        else:
            return {"status": 400, "error": "Error, missing user id, group chat id, or text"}
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
        self.__columns = ["id", "sender_id", "group_chat_id", "message_text", "time_sent", "read"]

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
            sql_string = """
            SELECT sender_id, users.name as sender_name, users.username as sender_username,
            message_text, time_sent, read
            FROM group_messages INNER JOIN users ON sender_id = users.id
            INNER JOIN group_memberships ON group_chat_id = group_chat_id
            WHERE group_chat_id = %(group_chat_id)s AND group_memberships.user_id = %(user_id)s;
            """
            args = {'user_id': user_id, 'group_chat_id': group_chat_id}

            if limit != None:
                sql_string += " LIMIT %(limit)s"
                args['limit'] = limit

            sql_data = exec_get_all(sql_string, args)
            result = jsonify_sql(sql_data, self.__columns)
            print(result)

            return result
        else:
            return {"status": 400, "error": "Error, no user id or receiever id provided"}
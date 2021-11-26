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

class Chats(Resource):
    def __init__(self):
        self.__columns = ["name", "last_message", "last_sent"]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        args = parser.parse_args()

        user_id = args["user_id"]

        if user_id != None:
            sql_string = """
                SELECT DISTINCT ON (username) username, message_text, time_sent FROM direct_messages
                INNER JOIN users ON receiver_id = users.id WHERE sender_id = %(user_id)s OR
                receiver_id = %(user_id)s GROUP BY username, message_text, time_sent
                UNION
                SELECT DISTINCT ON(name) name, message_text, time_sent FROM group_memberships INNER
                JOIN group_chats ON group_chats.id = group_id INNER JOIN group_messages ON
                group_chat_id = group_id WHERE user_id = %(user_id)s GROUP BY name, message_text, time_sent
                ORDER BY time_sent DESC
            """

            args = {'user_id': user_id}

            sql_data = exec_get_all(sql_string, args)
            result = jsonify_sql(sql_data, self.__columns)
            print(result)

            return result
        else:
            return {"status": 400, "error": "Error, no user id provided"}
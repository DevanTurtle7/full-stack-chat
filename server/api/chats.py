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
        self.__columns = ["id", "name", "last_message", "last_sent"]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        args = parser.parse_args()

        user_id = args["user_id"]

        if user_id != None:
            sql_string = """
                SELECT DISTINCT ON (name) users.id, name, message_text, time_sent
                FROM direct_messages INNER JOIN users ON
                    (CASE WHEN receiver_id = %(user_id)s THEN sender_id
                    WHEN sender_id = %(user_id)s THEN receiver_id END)
                = users.id
                WHERE receiver_id = %(user_id)s OR sender_id = %(user_id)s
                GROUP BY users.id, name, message_text, time_sent

                UNION

                SELECT DISTINCT ON (name) group_id, name, message_text, time_sent
                FROM group_memberships  INNER JOIN group_chats
                ON group_id = group_chats.id
                INNER JOIN group_messages ON group_id = group_chat_id
                WHERE user_id = %(user_id)s
                GROUP BY group_id, name, message_text, time_sent
                ORDER BY name, time_sent DESC;
            """

            args = {'user_id': user_id}

            sql_data = exec_get_all(sql_string, args)
            result = jsonify_sql(sql_data, self.__columns)
            print(result)

            return result
        else:
            return {"status": 400, "error": "Error, no user id provided"}
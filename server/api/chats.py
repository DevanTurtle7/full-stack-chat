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
        self.__columns = ["type", "id", "name", "last_message", "last_sent"]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        args = parser.parse_args()

        user_id = args["user_id"]

        if user_id != None:
            sql_string = """
                SELECT 'direct_message' as type, chats.id, users.name, message_text, chats.time_sent
                FROM (
                    SELECT (
                        CASE WHEN receiver_id = %(user_id)s THEN sender_id
                        WHEN sender_id = %(user_id)s THEN receiver_id END
                    ) as id, max(time_sent) as time_sent
                    FROM direct_messages INNER JOIN users ON (
                        CASE WHEN receiver_id = %(user_id)s THEN sender_id
                        WHEN sender_id = %(user_id)s THEN receiver_id END
                    ) = users.id
                    GROUP BY (
                        CASE WHEN receiver_id = %(user_id)s THEN sender_id
                        WHEN sender_id = %(user_id)s THEN receiver_id END
                    )
                ) as chats
                INNER JOIN direct_messages ON direct_messages.time_sent = chats.time_sent
                INNER JOIN users ON chats.id = users.id

                UNION

                SELECT DISTINCT ON (name) 'group_chat' as type, group_memberships.group_chat_id, name,
                message_text, time_sent
                FROM group_memberships INNER JOIN group_chats
                ON group_memberships.group_chat_id = group_chats.id
                INNER JOIN group_messages ON group_memberships.group_chat_id = group_messages.group_chat_id
                WHERE user_id = %(user_id)s
                GROUP BY group_memberships.group_chat_id, name, message_text, time_sent
                ORDER BY time_sent DESC;
            """

            args = {'user_id': user_id}

            sql_data = exec_get_all(sql_string, args)
            print(sql_data)
            result = jsonify_sql(sql_data, self.__columns)
            print(result)

            return result
        else:
            return {"status": 400, "error": "Error, no user id provided"}
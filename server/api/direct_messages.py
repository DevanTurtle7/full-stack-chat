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

class DirectMessages(Resource):
    def __init__(self):
        self.__columns = ["sender_id", "receiver_id", "other_name", "other_username", "message_text", "time_sent", "read"]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        parser.add_argument("receiver_id", type=int)
        parser.add_argument("limit", type=int)
        args = parser.parse_args()

        user_id = args["user_id"]
        receiver_id = args["receiver_id"]
        limit = args["limit"]

        if user_id != None and receiver_id != None:
            user_id = int(user_id)
            receiver_id = int(receiver_id)
            limit = int(limit)

            sql_string = """
                SELECT sender_id, receiver_id, users.name as other_name, users.username as other_username,
                message_text, time_sent, read
                FROM direct_messages INNER JOIN users ON
                    (CASE WHEN %(user_id)s = sender_id THEN receiver_id
                    WHEN %(user_id)s = receiver_id THEN sender_id END)
                = users.id
                WHERE %(user_id)s in (sender_id, receiver_id) and %(receiver_id)s in (sender_id, receiver_id) 
                ORDER BY time_sent DESC
            """
            args = {'user_id': user_id, 'receiver_id': receiver_id}

            if limit != None:
                sql_string += " LIMIT %(limit)s"
                args['limit'] = limit

            sql_data = exec_get_all(sql_string, args)
            result = jsonify_sql(sql_data, self.__columns)
            print(result)

            return result
        else:
            return {"status": 400, "error": "Error, no user id or receiever id provided"}
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        parser.add_argument("receiver_id", type=int)
        parser.add_argument("text", type=str)
        args = parser.parse_args()

        user_id = args["user_id"]
        receiver_id = args["receiver_id"]
        text = args["text"]

        if user_id != None and receiver_id != None and text != None:
            user_id = int(user_id)
            receiver_id = int(receiver_id)
            text = str(text)

            sql_string = """
                INSERT INTO direct_messages(sender_id, receiver_id, message_text) VALUES
                (%(user_id)s, %(receiver_id)s, %(message_text)s)
            """
            args = {'user_id': user_id, 'receiver_id': receiver_id, 'message_text': text}

            exec_commit(sql_string, args)

            return {"status": 201, "success": "Message was sent successfully"}
        else:
            return {"status": 400, "error": "Error, missing user id, receiever id, or text"}
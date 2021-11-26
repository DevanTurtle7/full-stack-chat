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
        self.__columns = ["id", "name", "last_message", "last_sent"]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", type=int)
        parser.add_argument("receiver_id", type=int)
        args = parser.parse_args()

        user_id = args["user_id"]
        receiver_id = args["receiver_id"]

        if user_id != None and receiver_id != None:
            sql_string = """

            """

            args = {'user_id': user_id, 'receiver_id': receiver_id}

            sql_data = exec_get_all(sql_string, args)
            result = jsonify_sql(sql_data, self.__columns)
            print(result)

            return result
        else:
            return {"status": 400, "error": "Error, no user id or receiever id provided"}
from flask_restful import Resource

from flask_restful import request
from flask_restful import reqparse
import json

# For testing/production
try:
    from server.utils.db_utils import *
except:
    from utils.db_utils import *

class Messages(Resource):
    def get(self):
        sql_string = """
            SELECT * FROM direct_messages WHERE sender_id = %(sender_id)s
            UNION
            SELECT * FROM group_messages WHERE sender_id = %(sender_id)s
        """
        args = {'sender_id': 1}

        result = exec_get_all(sql_string, args)

        print(result)

        return result


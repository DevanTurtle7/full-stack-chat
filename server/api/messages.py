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

class Messages(Resource):
    __slots__ = ['__columns']

    def __init__(self):
        self.__direct_messages_columns = ['id', 'sender_id', 'receiver_id', 'message_test', 'time_sent', 'read']
        self.__group_messages_columns = ['id', 'sender_id', 'receiver_id', 'message_test', 'time_sent', 'read']

    def __jsonify_sql(self, data, columns):
        """
        Converts sql data into JSON format

        Parameters:
            data: SQL data retrieved with psycopg
            columns: A list of column names, in the same order as the data
        """
        result = []

        if len(data) == 0: # Check if there is no data
            return [] # Return an empty list
        elif len(data) == 1: # Check if there is 1 object
            return dict(data) # Return an simply parsed json object
        else:
            for object in data:
                current = dict() # Create a hashmap for the current object to represent a json object

                for i in range(0, len(columns)): # Iterate the number of columns
                    column = columns[i] # Get the current column
                    value = object[i] # Get the current value

                    if isinstance(value, (datetime, date)): # Check if the value is a datetime object
                        value = value.isoformat() # Parse the datetime object
                    elif i == 2:
                        column = object[len(object) - 1]

                    current[column] = value # Create a key-value pair in the hashmap, with the key
                                            # being the column and the value being the value

                result.append(current) # Add the hashmap to the array
            
            return result # Return the array of json objects

    def get(self):
        sql_string = """
            SELECT *, 'receiver_id' AS receiver FROM direct_messages WHERE sender_id = %(sender_id)s
            UNION
            SELECT *, 'group_chat_id' AS receiver FROM group_messages WHERE sender_id = %(sender_id)s
        """
        args = {'sender_id': 1}
        sql_data = exec_get_all(sql_string, args)
        result = self.__jsonify_sql(sql_data, self.__direct_messages_columns)

        print(result)

        return result
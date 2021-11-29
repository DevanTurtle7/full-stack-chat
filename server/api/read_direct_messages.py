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

class ReadDirectMessages(Resource):
    def __init__(self):
        self.__columns = []

    def get(self):
        return {"status": 400, "error": "Error, route in unimplemented"}
    
    def post(self):
        return {"status": 400, "error": "Error, route in unimplemented"}
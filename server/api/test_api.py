from flask_restful import Resource

from flask_restful import request
from flask_restful import reqparse
import json
from .db_utils import *

class TestApi(Resource):
    def get(self):
        result = exec_get_all("SELECT * FROM direct_messages")
        return result


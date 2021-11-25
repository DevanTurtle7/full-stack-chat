from flask import Flask
from flask_restful import Resource, Api

if __name__ == '__main__':
    from api.db_utils import *
    from api.test_api import TestApi
else:
    from server.api.db_utils import *
    from server.api.test_api import TestApi

app = Flask(__name__) #create Flask instance

api = Api(app) #api router

api.add_resource(TestApi,'/api')

def rebuild_tables():
    exec_sql_file('server/api/schema.sql')

if __name__ == '__main__':
    print("Loading db");
    exec_sql_file('server/api/schema.sql');
    print("Starting flask");
    app.run(debug=True), #starts Flask



    
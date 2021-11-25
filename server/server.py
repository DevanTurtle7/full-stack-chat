from flask import Flask
from flask_restful import Resource, Api


from api.db_utils import *
from api.test_api import TestApi

app = Flask(__name__) #create Flask instance

api = Api(app) #api router

api.add_resource(TestApi,'/api')

if __name__ == '__main__':
    print("Loading db");
    exec_sql_file('server/api/schema.sql');
    print("Starting flask");
    app.run(debug=True), #starts Flask



    
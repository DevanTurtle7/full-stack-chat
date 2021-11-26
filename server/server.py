from flask import Flask
from flask_restful import Resource, Api

if __name__ == '__main__':
    from utils.db_utils import *
    from api.chats import Chats
else:
    from server.utils.db_utils import *
    from server.api.chats import Chats

app = Flask(__name__)
api = Api(app)

api.add_resource(Chats,'/chats')

def rebuild_tables():
    exec_sql_file('server/schema.sql')

if __name__ == '__main__':
    print("Loading db");
    exec_sql_file('server/schema.sql');
    exec_sql_file('tests/utils/test_data.sql')
    print("Starting flask");
    app.run(debug=True), #starts Flask



    
from flask import Flask
from flask_restful import Resource, Api

if __name__ == '__main__':
    from api.db_utils import *
    from api.messages import Messages
else:
    from server.api.db_utils import *
    from server.api.messages import Messages

app = Flask(__name__)
api = Api(app)

api.add_resource(Messages,'/messages')

def rebuild_tables():
    exec_sql_file('server/api/schema.sql')

if __name__ == '__main__':
    print("Loading db");
    exec_sql_file('server/api/schema.sql');
    print("Starting flask");
    app.run(debug=True), #starts Flask



    
from flask import Flask
from flask_restful import Resource, Api

if __name__ == '__main__':
    from utils.db_utils import *
    from api.chats import Chats
    from api.direct_messages import DirectMessages
    from api.group_messages import GroupMessages
else:
    from server.utils.db_utils import *
    from server.api.chats import Chats
    from server.api.direct_messages import DirectMessages
    from server.api.group_messages import GroupMessages

app = Flask(__name__)
api = Api(app)

api.add_resource(Chats,'/chats')
api.add_resource(DirectMessages,'/direct_messages')
api.add_resource(GroupMessages,'/group_messages')

def rebuild_tables():
    exec_sql_file('server/schema.sql')

if __name__ == '__main__':
    print("Loading db");
    exec_sql_file('server/schema.sql');
    exec_sql_file('tests/utils/test_data.sql')
    print("Starting flask");
    app.run(debug=True), #starts Flask



    
import unittest
from server.utils.db_utils import *
from server.server import rebuild_tables
from tests.utils.test_utils import *

class TestDBSchema(unittest.TestCase):

    def test_rebuild_tables(self):
        """Rebuild the tables"""
        rebuild_tables()
        assert_sql_count(self, "SELECT * FROM users", 0)
        assert_sql_count(self, "SELECT * FROM group_chats", 0)
        assert_sql_count(self, "SELECT * FROM group_memberships", 0)
        assert_sql_count(self, "SELECT * FROM direct_messages", 0)
        assert_sql_count(self, "SELECT * FROM group_messages", 0)

    def test_rebuild_tables_is_idempotent(self):
        """Drop and rebuild the tables twice"""
        rebuild_tables()
        rebuild_tables()
        assert_sql_count(self, "SELECT * FROM users", 0)
        assert_sql_count(self, "SELECT * FROM group_chats", 0)
        assert_sql_count(self, "SELECT * FROM group_memberships", 0)
        assert_sql_count(self, "SELECT * FROM direct_messages", 0)
        assert_sql_count(self, "SELECT * FROM group_messages", 0)

    def test_seed_data_works(self):
        """Attempt to insert the seed data"""
        rebuild_tables()
        insert_test_data()
        assert_sql_count(self, "SELECT * FROM users", 4)
        assert_sql_count(self, "SELECT * FROM group_chats", 2)
        assert_sql_count(self, "SELECT * FROM group_memberships", 7)
        assert_sql_count(self, "SELECT * FROM direct_messages", 9)
        assert_sql_count(self, "SELECT * FROM group_messages", 5)
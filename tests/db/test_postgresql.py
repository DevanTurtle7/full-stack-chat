import unittest
from server.api.db_utils import *
from tests.test_utils import *

class TestPostgreSQL(unittest.TestCase):

    def test_can_connect(self):
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT VERSION()')
        self.assertTrue(cur.fetchone()[0].startswith('PostgreSQL'))
        conn.close()
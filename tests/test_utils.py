import requests
from server.utils.db_utils import *

def insert_test_data():
    exec_sql_file('tests/test_data.sql')

def assert_sql_count(test, sql, n,
                     msg = 'Expected row count did not match query'):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    test.assertEqual(n, cur.rowcount, msg)
    conn.close()

def get_rest_call(test, url, params = {}, hdr = {}, expected_code = 200):
    response = requests.get(url, data=params, headers=hdr)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def post_rest_call(test, url, params = {}, hdr = {}, expected_code = 200):
    response = requests.post(url, data=params, headers=hdr)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def put_rest_call(test, url, params = {}, hdr = {}, expected_code = 200):
    response = requests.put(url, data=params, headers=hdr)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def delete_rest_call(test, url, params={}, hdr = {}, expected_code = 200):
    response = requests.delete(url, headers=hdr, data=params)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()
import unittest
import mock

# import psycopg2

# from mock_try import psycopg2
# import mock_try
from mock_try import data

class TestMyFunc(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch('mock_try.psycopg2', autospec=True) # Mocking psycopg2     
    @mock.patch('mock_try.cursor', autospec=True)    
    def test_myfunc(self, mock_cursor, mock_conn):
        mock_cursor.fetchone.return_value = (True,)
        res=data()
        print(res)
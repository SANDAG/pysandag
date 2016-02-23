import unittest
import os
from pysandag import database


class TestDatabaseMethods(unittest.TestCase):
    def test_get_connection_string(self):
        compare_string = 'mssql+pyodbc://user_name:a_password@sqlserverdatabase/a_database_name?driver=SQL+Server+Native+Client+11.0'
        self.assertEqual(database.get_connection_string('db.yml', 'in_db'), compare_string)

        cfg = {
                'in_db': {
                    'sql_alchemy_driver': 'mssql+pyodbc',
                    'driver': 'SQL+Server+Native+Client+11.0',
                    'host': 'sqlserverdatabase',
                    'database': 'a_database_name',
                    'port:': '',
                    'user': 'user_name',
                    'password': 'a_password'},
                'out_db': {
                    'sql_alchemy_driver': 'postgresql',
                    'driver': '',
                    'host': '',
                    'database': '',
                    'port': '',
                    'user': '',
                    'password': ''}
        }


if __name__ == '__main__':
    unittest.main()

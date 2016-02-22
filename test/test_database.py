import unittest

from pysandag import database


class TestDatabaseMethods(unittest.TestCase):
    def test_get_connection_string(self):
        compare_string = 'mssql+pyodbc://user_name:a_password@sqlserverdatabase/a_database_name?driver=SQL+Server+Native+Client+11.0'
        self.assertEqual(database.get_connection_string('../db.yml', 'in_db'), compare_string)


if __name__ == '__main__':
    unittest.main()

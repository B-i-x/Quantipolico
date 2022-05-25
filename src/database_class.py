import sqlite3
from sqlite3 import Error

class Database():

    def __init__(self, path: str) -> None:
        self.path = path

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            self.conn = sqlite3.connect(self.path)
            print('{} database connected'.format(self.path))
            return True
        except Error as e:
            print(e)
            return False

class DataTable():

    def __init__(self, db_connection, name: str) -> None:
        self.conn = db_connection
        self.name = name

    def setup(self, not_exists_check: bool, columns):
        '''columns must be formatted as follows:
        [[column_name_1, column_sql_datatype]...,[column_name_x, column_sql_datatype] ]'''
        query = "CREATE TABLE "
        if not_exists_check:
            query += "IF NOT EXISTS "
        
        query += f"{self.name} ("

        query += "id integer PRIMARY KEY, "

        for col in columns:
            col_name = col[0]
            datatype = col[1]

            query += f"{col_name} {datatype}, "
        
        query += ");"

        return query


def db_connect():

    path = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\src\db\main.db"

    directory_db = Database(path)

    if not directory_db.create_connection():
        return directory_db.conn
    else:
        return False




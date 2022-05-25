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

            query += f"{col_name} {datatype}"

            if col != columns[-1]:
                query += ","

            query += " "

        query += ");"

        return query

    def execute(self, sql_query):
        '''runs the sql query and prints the error if failed
        returns the cursor object if successful
        returns false if not'''
        try:
            cur = self.conn.cursor()
            cur.execute(sql_query)
            return cur

        except Error as e:
            print(e)
            return False

    def is_empty(self):
        '''checks if the table is empty
        returns true if is empty 
        returns false is NOT empty'''
        
        query = f"SELECT count(*) FROM (select 0 from {self.name} limit 1);"

        if self.execute(query).fetchone()[0] == 0:
            return True
        else: return False

    def is_valid(self):
        '''validates based on some requesities I will define at some point in my life
        returns true if valid
        false is not valid'''
        


def db_connect():

    path = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\src\db\main.db"

    directory_db = Database(path)

    if directory_db.create_connection():
        return directory_db.conn
    else:
        return False




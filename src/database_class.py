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

    def set_insert_columns(self,columns: list):
        """part of self.insert, the columns list should be a list of strings"""
        query = f"INSERT INTO {self.name} "
        
        query = "("
        for col in columns:

            query += f"{col}"

            if col != columns[-1]:
                query += ","

            query += " "

        query += ") VALUES "

    def set_insert_data(self, data: list, last = False):
        
        query = " ("
        for value in data:
            query += value

            if value != data[-1]:
                query += ","

        query += ")"

        if not last:
            query += ","
        else:
            query += ";"

        return query

    def insert(self, columns_query: str, values: str):

        insert_query = columns_query + values

        print(insert_query)
    


def db_connect():

    path = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\src\db\main.db"

    directory_db = Database(path)

    if directory_db.create_connection():
        return directory_db.conn
    else:
        return False




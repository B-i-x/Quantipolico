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

    def __set_insert_columns(self,columns: list):
        """part of self.insert, the columns list should be a list of strings"""
        query = f"INSERT INTO {self.name} "
        
        query += "("
        for col in columns:

            query += f"{col}"

            if col != columns[-1]:
                query += ","

            query += " "

        query += ") VALUES"

        return query

    def __set_insert_data(self, data: list, last = False):
        '''creates insert query for one row of data'''
        query = " ("
        for value in data:
            query += '"' + value + '"'

            if value != data[-1]:
                query += ","

        query += ")"

        if not last:
            query += ","
        else:
            query += ";"

        return query

    def insert_list(self, columns: list, data: list, committing=False):
        '''inserts the 2D list of data into the specified column(s)
        the naming of the columns must be a list of strings and must match the order of the 2d array
        ex:
        Columns[]: ["name", "state", "party", "district_number"]

        Data[]: [["John", "Arizo", "somet", "151251351551351"],
                  [["Smit", "Calif", "elseg", "651651023511033"]]
        '''
        col_query = self.__set_insert_columns(columns)

        data_query = ""

        for row in data:
            if row == data[-1]:
                data_query += self.__set_insert_data(row, last=True)
            else:
                data_query += self.__set_insert_data(row)

        insert_query = col_query + data_query

        if not committing:
            print(insert_query)
            
        else:
            self.execute(insert_query)
            self.conn.commit()

    def delete_self(self):

        query = f"DROP TABLE {self.name}"

        self.execute(query)
        self.conn.commit()
    
    def select_col_from_table(self, col: str):
        '''returns one column from a table in a list of tuples'''
        query = f"SELECT {col} FROM {self.name}"

        cur = self.conn.cursor()
        cur.execute(query)

        return cur.fetchall()

    def has_col_null(self, col: str):
        '''checks if column of table has any null
        returns true if there are nulls in table
        returns false if there are no nulls'''
        data = self.select_col_from_table(col)

        for tup_value in data:
            
            if tup_value == (None,):
                return True
        
        return False



def db_connect():

    path = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\src\db\main.db"

    directory_db = Database(path)

    if directory_db.create_connection():
        return directory_db.conn
    else:
        return False
import sqlite3
from sqlite3 import Error

'''
this file has all the sqllite related stuuff
'''
class Database():
    '''an interface with sqlite3 python package but handles the database part'''
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

    def delete_all_tables_except(directory_table):

        q = "SELECT 'DROP TABLE ' || name || ';' FROM sqlite_master WHERE type = 'table' AND name NOT IN ('X', 'Y', 'Z');"

class SQL_Query:
    '''handles sql queries in a more logical way i feel
    interface class for SQLlite3'''
    def __init__(self, database_connection) -> None:
        self.conn = database_connection
        self.query = None

    def execute(self):
        '''runs the sql query and prints the error if failed
        returns the cursor object if successful
        returns false if not'''

        if self.query is None:
            print("SQL Query not defined yet, cannot execute on empty query!")
            return

        try:
            cur = self.conn.cursor()
            cur.execute(self.query)
            return cur

        except Error as e:
            print(e)
            return False

    def commit(self):

        execution = self.execute()

        if not execution:
            print("SQL Execution Failed!")
            return

        self.conn.commit()

    def __str__(self) -> str:
        return self.query
    
    def print_query(self):
        print(self.query)

    def set(self, str_sql: str) -> None:

        self.query = str_sql

    def get(self, all: bool = True):
        '''returns object of sql query
        returns list by default'''
        cursor = self.execute()

        
        if not cursor or cursor is None:
            
            print("SQL Execution Failed!")

            return

        if all == False:
            return cursor.fetchone()

        else: return cursor.fetchall()
            
class DataTable():
    '''this class makes SQL_Query objects that are relevant to the dataTable
    honestly this is more like an sql generator
    inefficient because i am not generating a huge amount of similiar sql
    but it just makes things look nice when called in functions'''
    
    def __init__(self, db_connection, name: str) -> None:
        self.conn = db_connection
        self.name = name

        self.query = SQL_Query(db_connection)

    def setup(self, columns: list,not_exists_check: bool=True) -> SQL_Query:
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

        self.query.set(query)

        return self.query

    def is_empty(self) -> bool:
        '''checks if the table is empty
        returns true if is empty 
        returns false is NOT empty'''


        self.query.set(f"SELECT count(*) FROM (select 0 from {self.name} limit 1);")

        if self.query.execute().fetchone()[0] == 0:
            return True
        else: return False

    def __set_insert_columns(self,columns: list) -> str:
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

    def __set_insert_data(self, data: list, last = False) -> str:
        '''creates insert query_str for one row of data'''
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

    def insert_list_into_col(self, columns: list, data: list) -> SQL_Query:
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

        self.query.set(col_query + data_query)

        return self.query

    def delete_self(self) -> None:
        '''special cuz it commits'''
        self.query.set(f"DROP TABLE {self.name}")

        self.query.commit()
    
    def col_from_table(self, col: str, condition_col: str = None, condition: str = None) -> str:
        '''returns one column from a table in a list of tuples
        can also do conditions'''
        
        query = f"SELECT {col} FROM {self.name}"

        if not condition is None:
            query += f" WHERE {condition_col}"
            if condition == "NULL":
                query += f" IS NULL;"
            else:
                query += f"= {condition};"
         
        else:
            query += ";"

        self.query.set(query)

        return self.query

    def has_col_null(self, col: str) -> bool:
        '''checks if column of table has any null
        returns true if there are nulls in table
        returns false if there are no nulls'''
        data = self.col_from_table(col).get(all=True)

        if data is None:
            return True
        
        for tup_value in data:
            
            if tup_value == (None,):
                return True
        
        return False

    def insert_into_cell(self, data: str, insert_col: str, condition_col: str = None, condition: str=None) -> SQL_Query:
        '''inserts one piece of data into a row fulfulling the specified conditions'''

        query = f"UPDATE {self.name} SET {insert_col} = '{data}'"

        if not condition is None:
            query += f' WHERE {condition_col} = "{condition}";'

        else: query += f";"

        self.query.set(query)

        return self.query

    def cell_satisfying_condition(self, search_col: str, condition_col: str, condition: str) -> SQL_Query:

        query = str(self.col_from_table("name", "general_pressrelease_link", "NULL"))

        self.query.set(query[:len(query) - 1] + " ORDER BY id ASC LIMIT 1;")

        return self.query


def db_connect():

    path = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\src\db\main.db"

    directory_db = Database(path)

    if directory_db.create_connection():
        return directory_db.conn
    else:
        return False
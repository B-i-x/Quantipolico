from sqlite3 import Error
from sql_generation import Select

class SQL:

    def __init__(self, database_connection) -> None:

        self.db_conn = database_connection

        self.select = None

    def create_select(self) -> Select:

        self.select = Select()

        return self.select

    def clear(self):
        self.select = None

    def execute(self):
        '''runs the sql query and prints the error if failed
        returns the cursor object if successful
        returns false if not'''

        self.query = ""

        if self.query is None:
            print("SQL Query not defined yet, cannot execute on empty query!")
            return

        try:
            cur = self.db_conn.cursor()
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

        self.db_conn.commit()
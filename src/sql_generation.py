
from re import sub
from sqlite3 import Error

class Query_Generator():
    '''
    queries 
    SELECT 
    UPDATE

        sub-queries
        WHERE (can only be access from a select or update)
    '''
    def __init__(self, type = None) -> None:

        self.query_data = {}

        self.query = ""

        self.type = type

    def make_query(self) -> str:

        return self.query


class Where(Query_Generator):
    '''a type of addition to the select class'''
    def __init__(self, column: str) -> None:

        super().__init__("WHERE")

        self.col(column)

    def col(self, column: str) -> None:
        
        self.query_data["column"] = f" {column} "

    def is_value(self, value) -> None:

        self.query_data["operator"] = "="
        self.query_data["value"] = str(value)

    def has_values(self, values: list) -> None:

        self.query_data["operator"] = "IN"

        self.query_data["values"] = values

    def make_query(self) -> str:
        q = ""
        q += f'{self.query_data["column"]} {self.query_data["operator"]} '

        if "value" in self.query_data and "values" not in self.query_data:

            q += self.query_data["value"]
        
        else:

            q += "("
            for val in self.query_data["values"]:

                q += str(val)

                if val == self.query_data["values"][-1]:
                    q += ")"
                else:
                    q += ","

        return q

class Select(Query_Generator):

    def __init__(self) -> None:

        super().__init__("SELECT")
        

    def table(self, table_name: str) -> None:
        '''sets the table that the query will use'''

        self.query_data["table_name"] = table_name

    def columns(self, columns: list) -> None:
        '''sets the columns that query will search in'''

        self.query_data["columns"] = columns

    def where_paramater_for_col(self, column: str) -> Where:

        w = Where(column)

        if "WHERE" not in self.query_data:
            self.query_data["WHERE"] = []
        
        self.query_data["WHERE"].append(w)

        return w
        
    def make_query(self) -> str:

        q = "SELECT"

        for col in self.query_data["columns"]:

            q += " " + col

            if col != self.query_data["columns"][-1]:

                q += ","

        q += " " + f'FROM {self.query_data["table_name"]} '

        if "WHERE" in self.query_data:

            for parameter in self.query_data["WHERE"]:

                if parameter == self.query_data["WHERE"][0]: q = q + " WHERE "
                else: q += " AND "

                q += parameter.make_query()

            """TODO: #11 add query for other types of select parameters"""

        q += ";"

        self.query = q

        return q

class Update(Query_Generator):

    def __init__(self) -> None:
        super().__init__(type="UPDATE")

    def table(self, table_name : str) -> None:

        self.query_data["table_name"] = table_name

    def col(self, col_name: str) -> None:

        self.query_data["multiple_columns"] = False

        self.query_data["column"] = col_name

    def value(self, value) -> None:

        self.query_data["value"] = value

    def where_paramater_for_col(self, column: str) -> Where:

        w = Where(column)

        if "WHERE" not in self.query_data:
            self.query_data["WHERE"] = []
        
        self.query_data["WHERE"].append(w)

        return w

    def make_query(self) -> str:
        
        q = "UPDATE"

        q += f" {self.query_data['table_name']}"

        q += " SET"

        if not self.query_data["multiple_columns"]:

            q += f" {self.query_data['column']} = '{self.query_data['value']}'"

        if "WHERE" in self.query_data:

            for parameter in self.query_data["WHERE"]:

                if parameter == self.query_data["WHERE"][0]: q = q + " WHERE "
                else: q += " AND "

                q += parameter.make_query()

        return q

class Create_Table(Query_Generator):
    """TODO: #12 FINISH CREATE TABLE CLASS"""
    def __init__(self) -> None:
        super().__init__(type="CREATE_TABLE")

    def name(self, name: str):

        self.n = name

    def columns(self, columns: list) -> None:
        pass

    def make_query(self) -> str:
        pass

class Manual(Query_Generator):

    def __init__(self) -> None:
        super().__init__(type="Custom")

    def set(self, query: str) -> None:

        self.query = query

    def make_query(self) -> str:
        return super().make_query()

class SQL:

    def __init__(self, database_connection) -> None:

        self.db_conn = database_connection

    def create_select_query(self) -> Select:

        return Select()

    def create_table(self) -> Create_Table:

        return Create_Table()

    def create_update_query(self) -> Update:

        return Update()

    def clear(self):
        self.select = self.query = None

    def execute(self, query : str):
        '''runs the sql query and prints the error if failed
        returns the cursor object if successful
        returns false if not'''

        if query is None:
            print("SQL Query not defined yet, cannot execute on empty query!")
            return

        try:
            cur = self.db_conn.cursor()
            cur.execute(query)
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

    def get_result_from_query(self, query_generator_class: Query_Generator, return_type: str = "List of Strings", commit: bool= False):

        cursor = self.execute_query(query_generator_class)

        if return_type != "List of Strings":
            return cursor.fetchall()
        
        return ["".join(x) for x in cursor.fetchall()]

    def execute_query(self, query_generator_class: Query_Generator):

        qgc = query_generator_class
        query = qgc.make_query()

        print(query)

        cursor = self.execute(query)

        return cursor

    def commit_query(self, query_generator_class: Query_Generator):

        self.execute_query(query_generator_class)

        self.db_conn.commit()

    def print_query(self, query_generator_class: Query_Generator):

        print(query_generator_class.make_query())

        

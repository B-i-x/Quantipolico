from sqlite3_interface import DataTable, SQL_Query

class SELECT_Paramater():

    def __init__(self) -> None:
        self.query = ""

        self.type = ""

    def get_query(self) -> str:
        return self.query

class WHERE(SELECT_Paramater):

    def __init__(self, column: str) -> None:
        super().__init__()

        self.type = "WHERE"

        self.query = self.query + f" {column} "

    def is_value(self, value):

        self.query = self.query + f"= {value} "

    def has_values(self, values: list):

        self.query = self.query + f"IN ("

        for val in values:
            self.query = self.query + str(val)

            if val != values[-1]:
                self.query = self.query + ","

        self.query = self.query + ") "
            
    

class SELECT_Searcher():

    def __init__(self, database_connection) -> None:

        self.query_data = {
            "table_name": "",
            "columns" : []
        }

        self.query = "NULL QUERY"
        
        self.db_conn = database_connection

    def table(self, table_name: str) -> None:
        '''sets the table that the query will use'''

        self.query_data["table_name"] = table_name

    def columns(self, columns: list) -> None:
        '''sets the columns that query will search in'''

        self.query_data["columns"] = columns

    def add_parameter(self, param: SELECT_Paramater) -> None:

        if param.type not in self.query_data:
            self.query_data[param.type] = []

        self.query_data[param.type].append(param.get_query())
        

    def __make_query(self) -> SQL_Query:

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

                q += parameter

        q += ";"

        self.query = q

        obj = SQL_Query(self.db_conn)

        obj.set(q)

        return obj
    

    def get_result(self):
        sql = self.__make_query()

        return sql.get(return_type="List of Strings")


    def __str__(self) -> str:
        self.__make_query()
        
        return self.query
            
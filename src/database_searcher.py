from sqlite3_interface import DataTable, SQL_Query

class SELECT_Paramater():

    def __init__(self) -> None:
        self.query = ""

        self.type = ""

class WHERE(SELECT_Paramater):

    def __init__(self, column: str) -> None:
        super().__init__()

        self.type = "WHERE"

        self.query = self.query + " {column} "

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
        
        self.db_conn = database_connection

    def table(self, table_name: str) -> None:
        '''sets the table that the query will use'''

        self.query_data["table_name"] = table_name

    def columns(self, columns: list) -> None:
        '''sets the columns that query will search in'''

        self.query_data["columns"] = columns

    def add_parameter(self, param: SELECT_Paramater) -> None:

        parameter_num = str(len(self.query_data) - 2)
        
        self.query_data[param.type + parameter_num] = param.query
        

    def __make_query(self) -> SQL_Query:

        q = "SELECT"

        for col in self.query_data["columns"]:

            q = q + " " + col

            if col != self.query_data["columns"][-1]:

                q = q + ","

        q = q + " " + "FROM " + self.query_data["table_name"]

        extra_queries = []

        for query_type in self.query_data:

            if query_type != "columns" and query_type != "table_name":

                extra_queries.append(query_type)

        single_where_query = True

        for q in extra_queries:

            if "WHERE" in q:

                if single_where_query:

                    q = q + "WHERE" + self.query_data[q]

                else:

                    q = q + "AND" + self.query_data[q]

                single_where_query = False

        q = q + ";"

        self.query = q

        return SQL_Query(self.db_conn).set(q)
    

    def get_result(self):
        sql = self.__make_query()

        return sql.get()


    def __str__(self) -> str:
        print(self.__make_query())
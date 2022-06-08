from sqlite3_interface import DataTable, SQL_Query

class Paramater():

    def __init__(self, type: str = None) -> None:

        self.type = type

class Where(Paramater):

    def __init__(self, column: str) -> None:

        super().__init__("WHERE")

        self.query = f" {column} "

    def is_value(self, value) -> None:

        self.query += f"= {value} "

    def has_values(self, values: list) -> None:

        self.query += f"IN ("

        for val in values:
            self.query += str(val)

            if val != values[-1]:
                self.query += ","

        self.query += ") "
        

class Select():

    def __init__(self) -> None:

        super().__init__()

        self.query_data = {
            "table_name": "",
            "columns" : []
        }
        

    def table(self, table_name: str) -> None:
        '''sets the table that the query will use'''

        self.query_data["table_name"] = table_name

    def columns(self, columns: list) -> None:
        '''sets the columns that query will search in'''

        self.query_data["columns"] = columns

    def add_parameter(self, param: Paramater) -> None:

        if param.type not in self.query_data:
            self.query_data[param.type] = []

        self.query_data[param.type].append(param.query)
        
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

                q += parameter

            """TODO: #11 add query for other types of select parameters"""

        q += ";"

        return q

        


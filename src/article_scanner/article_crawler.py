
from src.sqlite3_interface import DataTable, Database

class article():

    def __init__(self):
        self.title = self.content = None
        
        self.day = self.month = self.year = None

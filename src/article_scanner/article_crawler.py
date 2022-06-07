
from src.sqlite3_interface import DataTable, Database


def load_articles(db_conn: Database, load: str) -> DataTable:
    pass

def search_and_load_articles(db_conn, load) -> str:
    '''returns 
    a code of diagnostics like new articles added and 
    success/failure codes'''
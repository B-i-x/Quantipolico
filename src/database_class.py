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


def directory_db_connect():

    path = r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\src\db\directory.db"

    directory_db = Database(path)

    if not directory_db.create_connection():
        return directory_db.conn
    else:
        return False




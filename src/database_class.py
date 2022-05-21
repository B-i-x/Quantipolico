from socket import create_connection
import sqlite3
from sqlite3 import Error

class Database():

    def __init__(self, path) -> None:
        self.path = path

        self.conn = None
        pass

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(self.path)
            print('{} database connected'.format(self.path))
        except Error as e:
            print(e)
        
        return conn

    def connect(self):
        conn = self.create_connection()
        
        if conn.total_changes == 0: 
            self.conn = conn
            return True

        else: 
            print("database connection failed!")
            return False
import sqlite3
from config import FILE_PATH_DATABASE

connection = sqlite3.connect(FILE_PATH_DATABASE)
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
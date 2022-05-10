import sqlite3
from config import DATABASE_FILE_PATH

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row

def get_database_connection():
    """Funktio, jonka avulla haetaan tietokantayhteys.

    Returns:
        Sqlite-olio, jonka avulla voidaan kirjoittaa ja lukea tietokantaa.
    """
    return connection
    
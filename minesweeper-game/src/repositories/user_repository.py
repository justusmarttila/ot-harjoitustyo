from entities.user import User
from connect_database import get_database_connection

def get_user_by_row(row):
    if row:
        return User(row["username"], row["password"])
    else:
        return None

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def fetch_all(self):

        db = self._connection.cursor()
        db.execute("select * from users")
        rows = db.fetchall()

        return list(map(get_user_by_row, rows))

    def fetch_by_username(self, username):
        db = self._connection.cursor()
        db.execute("select * from users where username = ?", (username,))

        row = db.fetchone()

        return get_user_by_row(row)

    def register(self, user):
        db = self._connection.cursor()
        db.execute("insert into users (username, password) values (?, ?)",
        (user.username, user.password))

        self._connection.commit()
        return user

    def clear_all(self):
        db = self._connection.cursor()
        db.execute("delete from users")
        self._connection.commit()

user_repo = UserRepository(get_database_connection())
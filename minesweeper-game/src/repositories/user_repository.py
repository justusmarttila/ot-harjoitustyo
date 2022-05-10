from entities.user import User
from connect_database import get_database_connection

def get_user(row):
    """Funktio, jonka avulla palautetaan User olio jos sellainen löytyy.

    Args:
        row (sqlite3 data): Tietokannasta haettu data.

    Returns:
        User: User-olio jatko käyttöä varten.
    """

    if row:
        return User(row["username"], row["password"])
    return None

class UserRepository:
    """Luokka, joka vastaa tietokantaan liittyvistä toimenpiteistä.
    """

    def __init__(self, connection):
        """Luokan konstruktori, jolle annetaan tietokanta yhteys, jolle operaatiot toteutetaan.

        Args:
            connection (Connection-olio): Tietokantayhteyden luomista varten.
        """

        self._connection = connection

    def fetch_all(self):
        """Funktio, joka hakee kaikki käyttäjät tietokannasta.

        Returns:
            list: Palauttaa listan kaikista käyttäjistä User-olioina.
        """

        db = self._connection.cursor()
        db.execute("select * from users")
        rows = db.fetchall()

        return list(map(get_user, rows))

    def fetch_by_username(self, username):
        """Funktio, jonka avaulla katsotaan onko tietty käyttäjätunnus jo tietokannassa.

        Args:
            username (Str): Käyttäjätunnus, jonka olemassa olo tietokannassa tarkistetaan.

        Returns:
            User: Palauttaa User-oliona käyttäjän, jos sellainen löytyy muuten None.
        """

        db = self._connection.cursor()
        db.execute("select * from users where username = ?", (username,))

        row = db.fetchone()

        return get_user(row)

    def register(self, user):
        """Funktio, jonka avulla rekisteröidään käyttäjä tietokantaan
        eli lisätään users tauluun käyttäjätunnus-salasana pari.

        Args:
            user (User-olio): Käyttäjä, joka lisätään.

        Returns:
            User: Palauttaa lisätyn käyttäjän.
        """

        db = self._connection.cursor()
        db.execute("insert into users (username, password) values (?, ?)",
        (user.username, user.password))

        self._connection.commit()
        return user

    def clear_all(self):
        """Funktio, joka tyhjentää users taulun.
        """

        db = self._connection.cursor()
        db.execute("delete from users")
        self._connection.commit()

user_repo = UserRepository(get_database_connection())

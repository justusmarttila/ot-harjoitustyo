from entities.user import User

from repositories.user_repository import (
    user_repo as default_user_repo
)

class InvalidUsernameOrPasswordError(Exception):
    """Epäkelvon käyttäjätunnuksen tai salasanan syöttämisestä nostettava virhe.

    Args:
        Exception (Str): Esitettävä virheviesti.
    """

    pass

class UsernameAlreadyExistsError(Exception):
    """Luokka, joka vastaa käyttäjätunnus on jo käytössä virheen nostamisesta.

    Args:
        Exception (Str): Esitettävä virheviesti.
    """

    pass

class UIService:
    """Luokka, joka vastaa käyttäjien rekisteröimisestä ja kirjautumisesta.
    """

    def __init__(self, user_repo=default_user_repo):
        """Konstruktori, jolle annetaan tietokanta toiminnoista vastaava luokka.

        Args:
            user_repo (UserRepository-olio): Luokka, jossa tietokantaan liittyvät operaatiot.
        """
        self._user_repo = user_repo

    def login(self, username, password):
        """Funktio, jonka avulla kirjataan käyttäjä sisään, jos tiedot löytyvät tietokannasta.

        Args:
            username (Str): Käyttäjän väh. 3 merkin pituinen käyttäjätunnus.
            password (Str): Käyttäjän salasana.

        Raises:
            InvalidUsernameOrPasswordError: Syötetyt tiedot eivät löydy tietokannasta.
        """

        user = self._user_repo.fetch_by_username(username)

        if not user or user.password != password:
            raise InvalidUsernameOrPasswordError("Invalid username or password, try again")

    def register_user(self, username, password):
        """Funktio, joka rekisteröi käyttäjän tietokantaan.

        Args:
            username (Str): Käyttäjän väh. 3 merkin pituinen käyttäjätunnus.
            password (Str): Käyttäjän salasana.

        Raises:
            UsernameAlreadyExistsError: Käyttäjätunnus on jo käytössä.
        """

        already_existing = self._user_repo.fetch_by_username(username)

        if already_existing:
            raise UsernameAlreadyExistsError("This username already exists, try again")

        self._user_repo.register(User(username, password))

UI_service = UIService()

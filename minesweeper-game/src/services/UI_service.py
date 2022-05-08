from entities.user import User

from repositories.user_repository import (
    user_repo as default_user_repo
)

class InvalidUsernameOrPasswordError(Exception):
    pass

class UsernameAlreadyExistsError(Exception):
    pass

class UIService:
    def __init__(self, user_repo=default_user_repo):
        self._user = None
        self._user_repo = user_repo

    def login(self, username, password):

        user = self._user_repo.fetch_by_username(username)

        if not user or user.password != password:
            raise InvalidUsernameOrPasswordError("Invalid username or password, try again")

        self._user = user

        return user

    def get_all_users(self):
        return self._user_repo.fetch_all()

    def get_current_user(self):
        return self._user

    def logout(self):
        self._user = None

    def register_user(self, username, password, login=True):

        already_existing = self._user_repo.fetch_by_username(username)

        if already_existing:
            raise UsernameAlreadyExistsError("This username already exists, try again")

        user = self._user_repo.register(User(username, password))

        if login:
            self._user = user

        return user

UI_service = UIService()

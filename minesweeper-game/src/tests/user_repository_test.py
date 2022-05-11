import unittest
from repositories.user_repository import user_repo
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repo.clear_all()

        self.user_aaron = User("aaron", "mitaikina")
        self.user_kyyhkynen = User("kyyhkynen", "nautiwa")

        user_repo.register(self.user_aaron)

    def test_register(self):

        self.assertEqual("aaron", self.user_aaron.username)

    def test_fetch_by_username(self):

        user = user_repo.fetch_by_username(self.user_aaron.username)

        self.assertEqual(user.username, self.user_aaron.username)

    def test_fetch_all(self):
        all_users = user_repo.fetch_all()

        self.assertEqual(len(all_users), 1)

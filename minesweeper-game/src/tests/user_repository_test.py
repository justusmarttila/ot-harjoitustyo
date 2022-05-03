"""import unittest
from repositories.user_repository import user_repo
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repo.clear_all()

        self.user_aaron = User("aaron", "mitaikina")
        self.user_kyyhkynen = User("kyyhkynen", "nautiwa")

    def test_create(self):
        user_repo.create(self.user_aaron)
        all_users = user_repo.fetch_all()

        self.assertEqual(len(all_users), 1)
        self.assertEqual(all_users[0].username, self.user_aaron.username)

    def test_fetch_by_username(self):
        user_repo.create(self.user_aaron)

        user = user_repo.fetch_by_username(self.user_aaron.username)

        self.assertEqual(user.username, self.user_aaron.username)"""

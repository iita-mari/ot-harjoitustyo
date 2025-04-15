import unittest
import os
from repositories.user_repository import User, UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        if os.path.exists("data/test_users.csv"):
            os.remove("data/test_users.csv")
        self.user_repository = UserRepository("data/test_users.csv")
        self.user_matti = User('matti', 'matti1')
        self.user_maija = User('maija', 'maija1')

    def test_create(self):
        self.user_repository.create(self.user_matti)
        users = self.user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_matti.username)

    def test_find_all(self):
        self.user_repository.create(self.user_matti)
        self.user_repository.create(self.user_maija)
        users = self.user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, 'matti')
        self.assertEqual(users[1].username, 'maija')

    def test_find_by_username(self):
        self.user_repository.create(self.user_matti)
        user = self.user_repository.find_by_username(self.user_matti.username)
        self.assertEqual(user.username, self.user_matti.username)
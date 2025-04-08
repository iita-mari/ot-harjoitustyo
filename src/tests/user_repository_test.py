import unittest
from repositories.user_repository import User
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_kalle = User('matti', 'matti1')
        self.user_matti = User('maija', 'maija1')
        self.user_repository = UserRepository


    def test_create(self):
        UserRepository.create(self.user_repository)
        a = UserRepository.find_all()

        self.assertEqual(len(a), 1)
        self.assertEqual(a[0].content, self.user_repository.content)

    def test_find_all(self):
        UserRepository.create(self.user_repository)
        a = UserRepository.find_all()

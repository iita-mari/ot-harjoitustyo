import unittest
import os
from repositories.housework_repository import HouseworkRepository


class TestHouseworkRepository(unittest.TestCase):
    def setUp(self):
        self.housework = HouseworkRepository()
        self.test_username = "testi"
        self.test_housework = self.housework._get_user_file(self.test_username)
        if os.path.exists(self.test_housework):
            os.remove(self.test_housework)

        if os.path.exists(self.test_housework):
            os.remove(self.test_housework)

    def test_add(self):
        self.housework.add(self.test_username, "imurointi")
        tasks = self.housework.get_all(self.test_username)
        self.assertIn("imurointi", tasks)


import unittest
from ui.ui import UI


class TestUi(unittest.TestCase):
    def setUp(self):
        self.ui = UI()

    def test_exit_login(self):
        self.ui.exit_login()
        self.assertEqual(str(self.ui.exit_login()), "Kiitos ja näkemiin!")
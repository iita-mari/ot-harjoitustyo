import unittest
from luetutapp import Ui


class TestUi(unittest.TestCase):
    def setUp(self):
        self.ui = Ui()

    def test_exit_login(self):
        self.ui.exit_login()
        self.assertEqual(str(self.exit_login()), "Kiitos ja näkemiin!")

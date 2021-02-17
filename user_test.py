import unittest
from user import Users
from user import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = Users("Jean", "Jaybe")
    def test_init(self):
        self.assertEqual(self.new_user.username, "Jean")
        self.assertEqual(self.new_user.password, "Jaybe")

    def test_login(self):
        self.assertTrue(self.new_user.username, 'Jean')
        self.assertTrue(self.new_user.password, 'Jaybe')    

    def test_delete(self):
        self.assertTrue(self.new_user.username, 'Jean')
        self.assertTrue(self.new_user.password, 'Jaybe') 

    def test_create(self):
        self.assertTrue(self.new_user.username, 'Jean')
        self.assertTrue(self.new_user.password, 'Jaybe')  

if __name__ == '__main__':
    unittest.main()        
import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        User.emails = set()

    def test_add_user(self):
        user = User(email="betty@gmail.com", first_name="Betty", last_name="Jan", password="ok")
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, "betty@gmail.com")

    def test_unique_email(self):
        User.emails = set()
        user1 = User(email="unique@gmail.com", first_name="Pyco", last_name="Jan", password="ok")
        with self.assertRaises(ValueError):
            user2 = User(email="unique@gmail.com", first_name="Betty", last_name="Jan", password="ok")

if __name__ == '__main__':
    unittest.main()

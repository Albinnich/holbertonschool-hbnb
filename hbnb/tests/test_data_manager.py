import unittest
from models.user import User
from persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        User.emails = set()
        self.data_manager = DataManager()
        self.user = User(email="betty@gmail.com", first_name="Betty", last_name="Jan", password="ok")
        self.data_manager.save(self.user)

    def test_save(self):
        user = self.data_manager.get(self.user.id, "User")
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "betty@gmail.com")

    def test_get(self):
        user = self.data_manager.get(self.user.id, "User")
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, "Betty")

    def test_update(self):
        self.user.first_name = "Betty"
        self.data_manager.update(self.user)
        updated_user = self.data_manager.get(self.user.id, "User")
        self.assertEqual(updated_user.first_name, "Betty")

    def test_delete(self):
        self.data_manager.delete(self.user.id, "User")
        user = self.data_manager.get(self.user.id, "User")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()

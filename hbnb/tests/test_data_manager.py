import unittest
from persistence.data_manager import DataManager
from models.user import User
import os

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('test_data.json')

    def tearDown(self):
        if os.path.exists('test_data.json'):
            os.remove('test_data.json')

    def test_save_and_get_user(self):
        user = User(email="test@example.com", password="test", first_name="Test", last_name="User")
        self.data_manager.save(user)
        retrieved_user = self.data_manager.get(user.id, 'User')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['email'], "test@example.com")

    def test_update_user(self):
        user = User(email="test@example.com", password="test", first_name="Test", last_name="User")
        self.data_manager.save(user)
        user.first_name = "UpdatedName"
        self.data_manager.update(user)
        retrieved_user = self.data_manager.get(user.id, 'User')
        self.assertEqual(retrieved_user['first_name'], "UpdatedName")

    def test_delete_user(self):
        user = User(email="test@example.com", password="test", first_name="Test", last_name="User")
        self.data_manager.save(user)
        self.data_manager.delete(user.id, 'User')
        retrieved_user = self.data_manager.get(user.id, 'User')
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()

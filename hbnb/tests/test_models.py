import unittest
from yourapp.models import User, db
from yourapp import create_app

class TestUserModel(unittest.TestCase):

    def setUp(self):
        """ Set up test environment """
        self.app = create_app(config='testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """ Clean up after tests """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        """ Test user creation """
        user = User(email='test@example.com', password='test_password', 
                    first_name='John', last_name='Doe')
        db.session.add(user)
        db.session.commit()
        self.assertIsNotNone(user.id)
        # Add more assertions to test user properties and relationships

    # Add more tests for other models and their interactions

if __name__ == '__main__':
    unittest.main()

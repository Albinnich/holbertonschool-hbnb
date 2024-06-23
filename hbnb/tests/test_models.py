import unittest
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.country import Country

class TestModels(unittest.TestCase):
    def test_user_creation(self):
        user = User(email="test@example.com", password="test", first_name="Test", last_name="User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "Test")

    def test_place_creation(self):
        user = User(email="host@example.com", password="test", first_name="Host", last_name="User")
        place = Place(name="Test Place", description="A place for testing", address="123 Test St", city="Testville",
                      latitude=10.0, longitude=20.0, host=user, num_rooms=2, bathrooms=1, price_per_night=100, max_guests=4)
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.host.email, "host@example.com")

    def test_review_creation(self):
        user = User(email="reviewer@example.com", password="test", first_name="Reviewer", last_name="User")
        place = Place(name="Test Place", description="A place for testing", address="123 Test St", city="Testville",
                      latitude=10.0, longitude=20.0, host=user, num_rooms=2, bathrooms=1, price_per_night=100, max_guests=4)
        review = Review(user=user, place=place, rating=5, comment="Great place!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Great place!")

if __name__ == '__main__':
    unittest.main()

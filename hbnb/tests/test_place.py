import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def test_add_place(self):
        place = Place(name="Ideal Island", description="Nice place", number_rooms=2, max_guest=4, price_by_night=100, user_id="user123", city_id="city123")
        self.assertIsNotNone(place.id)
        self.assertEqual(place.name, "Ideal Island")

if __name__ == '__main__':
    unittest.main()

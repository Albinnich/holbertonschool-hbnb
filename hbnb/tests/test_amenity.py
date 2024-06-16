import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_add_amenity(self):
        amenity = Amenity(name="Parking")
        self.assertIsNotNone(amenity.id)
        self.assertEqual(amenity.name, "Parking")

if __name__ == '__main__':
    unittest.main()

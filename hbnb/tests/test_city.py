import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_add_city(self):
        city = City(name="Suva", country_id="123")
        self.assertIsNotNone(city.id)
        self.assertEqual(city.name, "Suva")
        self.assertEqual(city.country_id, "123")

if __name__ == '__main__':
    unittest.main()

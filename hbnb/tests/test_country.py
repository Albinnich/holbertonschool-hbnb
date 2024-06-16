import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def test_add_country(self):
        country = Country(name="Fiji")
        self.assertIsNotNone(country.id)
        self.assertEqual(country.name, "Fiji")

if __name__ == '__main__':
    unittest.main()

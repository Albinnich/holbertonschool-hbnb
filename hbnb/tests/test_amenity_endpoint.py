import unittest
import json
from app import app, data_manager
from models.amenity import Amenity

class TestAmenityEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        data_manager.storage = {}

    def test_create_amenity(self):
        response = self.app.post('/amenities', data=json.dumps({'name': 'WiFi'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('WiFi', str(response.data))

    def test_get_all_amenities(self):
        amenity = Amenity(name='WiFi')
        data_manager.save(amenity)
        response = self.app.get('/amenities')
        self.assertEqual(response.status_code, 200)
        self.assertIn('WiFi', str(response.data))

    def test_get_single_amenity(self):
        amenity = Amenity(name='WiFi')
        data_manager.save(amenity)
        response = self.app.get(f'/amenities/{amenity.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('WiFi', str(response.data))

    def test_update_amenity(self):
        amenity = Amenity(name='WiFi')
        data_manager.save(amenity)
        response = self.app.put(f'/amenities/{amenity.id}', data=json.dumps({'name': 'High-Speed WiFi'}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('High-Speed WiFi', str(response.data))

    def test_delete_amenity(self):
        amenity = Amenity(name='WiFi')
        data_manager.save(amenity)
        response = self.app.delete(f'/amenities/{amenity.id}')
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(data_manager.get(amenity.id, 'Amenity'))

if __name__ == '__main__':
    unittest.main()

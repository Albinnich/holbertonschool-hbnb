import unittest
import json
from app import app
from app.persistence.data_manager import DataManager

class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        DataManager().storage = {"Amenity": {}}

    def test_create_amenity(self):
        response = self.app.post('/amenities/', data=json.dumps({'name': 'WiFi'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_all_amenities(self):
        response = self.app.get('/amenities/')
        self.assertEqual(response.status_code, 200)

    def test_get_single_amenity(self):
        post_response = self.app.post('/amenities/', data=json.dumps({'name': 'Pool'}), content_type='application/json')
        amenity_id = json.loads(post_response.data)['id']
        get_response = self.app.get(f'/amenities/{amenity_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertIn('name', json.loads(get_response.data))

    def test_update_amenity(self):
        post_response = self.app.post('/amenities/', data=json.dumps({'name': 'Parking'}), content_type='application/json')
        amenity_id = json.loads(post_response.data)['id']
        put_response = self.app.put(f'/amenities/{amenity_id}', data=json.dumps({'name': 'Free Parking'}), content_type='application/json')
        self.assertEqual(put_response.status_code, 200)
        self.assertIn('Free Parking', json.loads(put_response.data)['name'])

    def test_delete_amenity(self):
        post_response = self.app.post('/amenities/', data=json.dumps({'name': 'Breakfast'}), content_type='application/json')
        amenity_id = json.loads(post_response.data)['id']
        delete_response = self.app.delete(f'/amenities/{amenity_id}')
        self.assertEqual(delete_response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

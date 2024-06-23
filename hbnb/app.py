from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
import uuid

app = Flask(__name__)
api = Api(app, version='1.0', title='Places Management API',
          description='APIs for managing places, cities, and amenities.')

# Dummy data structures for demo (replace with actual database operations)
cities = [{'id': '1', 'name': 'New York'}, {'id': '2', 'name': 'San Francisco'}]
places = []
amenities = [{'id': '1', 'name': 'WiFi'}, {'id': '2', 'name': 'Pool'}]

# Define data models
place_model = api.model('Place', {
    'name': fields.String(required=True, description='Place name'),
    'description': fields.String(required=True, description='Place description'),
    'address': fields.String(required=True, description='Place address'),
    'city_id': fields.String(required=True, description='ID of the city where place is located'),
    'latitude': fields.Float(required=True, description='Geographical latitude'),
    'longitude': fields.Float(required=True, description='Geographical longitude'),
    'host_id': fields.String(description='ID of the host'),
    'number_of_rooms': fields.Integer(required=True, description='Number of rooms'),
    'number_of_bathrooms': fields.Integer(required=True, description='Number of bathrooms'),
    'price_per_night': fields.Float(required=True, description='Price per night'),
    'max_guests': fields.Integer(required=True, description='Maximum number of guests'),
    'amenity_ids': fields.List(fields.String, description='List of amenity IDs')
})

# Endpoint implementations
@api.route('/places')
class Places(Resource):
    @api.marshal_with(place_model)
    def get(self):
        """Retrieve all places"""
        return places

    @api.expect(place_model, validate=True)
    @api.response(201, 'Place successfully created.')
    def post(self):
        """Create a new place"""
        data = request.json
        # Validate data here (implement according to requirements)
        # Simulate ID generation for demo
        data['id'] = str(uuid.uuid4())
        places.append(data)
        return data, 201

@api.route('/places/<string:place_id>')
class Place(Resource):
    @api.marshal_with(place_model)
    def get(self, place_id):
        """Retrieve details of a specific place"""
        for place in places:
            if place['id'] == place_id:
                return place
        api.abort(404, f"Place {place_id} not found")

    @api.expect(place_model, validate=True)
    @api.response(204, 'Place successfully updated.')
    def put(self, place_id):
        """Update details of a specific place"""
        data = request.json
        for index, place in enumerate(places):
            if place['id'] == place_id:
                places[index] = data
                return '', 204
        api.abort(404, f"Place {place_id} not found")

    @api.response(204, 'Place successfully deleted.')
    def delete(self, place_id):
        """Delete a specific place"""
        for index, place in enumerate(places):
            if place['id'] == place_id:
                del places[index]
                return '', 204
        api.abort(404, f"Place {place_id} not found")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

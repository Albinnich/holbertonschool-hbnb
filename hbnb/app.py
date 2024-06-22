from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from models.amenity import Amenity
from persistence.data_manager import DataManager

app = Flask(__name__)
api = Api(app, version='1.0', title='HBnB API', description='Amenity Management API')

data_manager = DataManager()

# Define Amenity Model for API documentation
amenity_model = api.model('Amenity', {
    'id': fields.String(readOnly=True, description='The unique identifier of an amenity'),
    'name': fields.String(required=True, description='Amenity name'),
    'created_at': fields.DateTime(readOnly=True, description='Time when the amenity was created'),
    'updated_at': fields.DateTime(readOnly=True, description='Time when the amenity was last updated')
})

@api.route('/amenities')
class AmenityList(Resource):
    @api.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        return data_manager.list('Amenity')

    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created.')
    @api.response(409, 'Amenity name already exists.')
    def post(self):
        """Create a new amenity"""
        data = request.json
        if data_manager.list('Amenity'):
            for amenity in data_manager.list('Amenity'):
                if amenity.name == data['name']:
                    return {'message': 'Amenity name already exists'}, 409
        new_amenity = Amenity(name=data['name'])
        data_manager.save(new_amenity)
        return new_amenity, 201

@api.route('/amenities/<string:amenity_id>')
class Amenity(Resource):
    @api.marshal_with(amenity_model)
    @api.response(404, 'Amenity not found.')
    def get(self, amenity_id):
        """Retrieve a specific amenity by its ID"""
        amenity = data_manager.get(amenity_id, 'Amenity')
        if amenity:
            return amenity
        return {'message': 'Amenity not found'}, 404

    @api.expect(amenity_model)
    @api.response(200, 'Amenity successfully updated.')
    @api.response(404, 'Amenity not found.')
    def put(self, amenity_id):
        """Update an existing amenity"""
        data = request.json
        amenity = data_manager.get(amenity_id, 'Amenity')
        if amenity:
            amenity.name = data['name']
            amenity.save()
            data_manager.update(amenity)
            return amenity, 200
        return {'message': 'Amenity not found'}, 404

    @api.response(204, 'Amenity successfully deleted.')
    @api.response(404, 'Amenity not found.')
    def delete(self, amenity_id):
        """Delete a specific amenity by its ID"""
        if data_manager.get(amenity_id, 'Amenity'):
            data_manager.delete(amenity_id, 'Amenity')
            return '', 204
        return {'message': 'Amenity not found'}, 404

if __name__ == '__main__':
    app.run(debug=True)

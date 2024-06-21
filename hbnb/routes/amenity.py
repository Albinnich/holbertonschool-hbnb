from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager

app = Flask(__name__)
api = Api(app, version='1.0', title='Amenity API',
          description='A simple Amenity API')

ns = api.namespace('amenities', description='Amenities operations')

data_manager = DataManager()

amenity_model = api.model('Amenity', {
    'id': fields.String(readOnly=True, description='The unique identifier of an amenity'),
    'name': fields.String(required=True, description='Amenity name')
})

@ns.route('/')
class AmenityList(Resource):
    @ns.doc('list_amenities')
    @ns.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        amenities = data_manager.get_all('Amenity')
        return amenities

    @ns.doc('create_amenity')
    @ns.expect(amenity_model)
    @ns.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        data = request.json
        name = data.get('name')
        if not name:
            api.abort(400, "Amenity name is required")
        try:
            amenity = Amenity(name=name)
            data_manager.save(amenity)
            return amenity, 201
        except ValueError as e:
            api.abort(409, str(e))

@ns.route('/<string:amenity_id>')
@ns.response(404, 'Amenity not found')
@ns.param('amenity_id', 'The amenity identifier')
class Amenity(Resource):
    @ns.doc('get_amenity')
    @ns.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Fetch an amenity given its identifier"""
        amenity = data_manager.get(amenity_id, 'Amenity')
        if amenity is None:
            api.abort(404, "Amenity not found")
        return amenity

    @ns.doc('delete_amenity')
    @ns.response(204, 'Amenity deleted')
    def delete(self, amenity_id):
        """Delete an amenity given its identifier"""
        amenity = data_manager.get(amenity_id, 'Amenity')
        if amenity is None:
            api.abort(404, "Amenity not found")
        data_manager.delete(amenity_id, 'Amenity')
        return '', 204

    @ns.expect(amenity_model)
    @ns.marshal_with(amenity_model)
    def put(self, amenity_id):
        """Update an amenity given its identifier"""
        data = request.json
        name = data.get('name')
        if not name:
            api.abort(400, "Amenity name is required")

        amenity = data_manager.get(amenity_id, 'Amenity')
        if amenity is None:
            api.abort(404, "Amenity not found")

        if name != amenity.name and name in Amenity.names:
            api.abort(409, "Name must be unique")

        amenity.name = name
        amenity.save()
        data_manager.update(amenity)
        return amenity

if __name__ == '__main__':
    app.run(debug=True)

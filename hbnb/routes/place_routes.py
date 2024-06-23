# place_routes.py

from flask import Blueprint, request, jsonify
from models.place import Place
from data_manager import DataManager

place_bp = Blueprint('place', __name__, url_prefix='/places')
data_manager = DataManager()

@place_bp.route('', methods=['POST'])
def create_place():
    data = request.json
    required_fields = ['name', 'description', 'address', 'city_id', 'latitude', 'longitude',
                       'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests', 'amenity_ids']

    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400

    # Validate numerical fields
    numerical_fields = ['latitude', 'longitude', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests']
    for field in numerical_fields:
        if not isinstance(data[field], (int, float)):
            return jsonify({'error': f'{field} must be a number'}), 400

    # Validate city_id
    city_id = data.get('city_id')
    if not data_manager.get_city_by_id(city_id):
        return jsonify({'error': 'Invalid city_id'}), 400

    # Validate amenity_ids
    amenity_ids = data.get('amenity_ids', [])
    for amenity_id in amenity_ids:
        if not data_manager.get_amenity_by_id(amenity_id):
            return jsonify({'error': f'Amenity with ID {amenity_id} does not exist'}), 400

    new_place = Place(**data)
    data_manager.save_place(new_place)

    return jsonify(new_place.to_dict()), 201

@place_bp.route('', methods=['GET'])
def get_places():
    places = data_manager.get_places()
    return jsonify([place.to_dict() for place in places]), 200

@place_bp.route('/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = data_manager.get_place_by_id(place_id)
    if place:
        return jsonify(place.to_dict()), 200
    else:
        return jsonify({'error': 'Place not found'}), 404

@place_bp.route('/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.json
    place = data_manager.get_place_by_id(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    # Validate numerical fields if present
    numerical_fields = ['latitude', 'longitude', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests']
    for field in numerical_fields:
        if field in data and not isinstance(data[field], (int, float)):
            return jsonify({'error': f'{field} must be a number'}), 400

    # Validate city_id if present
    city_id = data.get('city_id')
    if city_id and not data_manager.get_city_by_id(city_id):
        return jsonify({'error': 'Invalid city_id'}), 400

    # Validate amenity_ids if present
    amenity_ids = data.get('amenity_ids', [])
    for amenity_id in amenity_ids:
        if not data_manager.get_amenity_by_id(amenity_id):
            return jsonify({'error': f'Amenity with ID {amenity_id} does not exist'}), 400

    # Update place fields
    for key, value in data.items():
        setattr(place, key, value)

    data_manager.update_place(place)

    return jsonify(place.to_dict()), 200

@place_bp.route('/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = data_manager.get_place_by_id(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    data_manager.delete_place(place_id)
    return jsonify(), 204

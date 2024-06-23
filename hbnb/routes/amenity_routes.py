from flask import Blueprint, request, jsonify
from models.amenity import Amenity
from data_manager import DataManager

amenity_bp = Blueprint('amenity', __name__, url_prefix='/amenities')
data_manager = DataManager()

@amenity_bp.route('', methods=['POST'])
def create_amenity():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    existing_amenities = data_manager.get_amenities()
    for amenity in existing_amenities:
        if amenity.name == name:
            return jsonify({'error': 'Amenity with this name already exists'}), 409

    new_amenity = Amenity(name=name)
    data_manager.save_amenity(new_amenity)

    return jsonify(new_amenity.to_dict()), 201

@amenity_bp.route('', methods=['GET'])
def get_amenities():
    amenities = data_manager.get_amenities()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

@amenity_bp.route('/<int:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = data_manager.get_amenity_by_id(amenity_id)
    if amenity:
        return jsonify(amenity.to_dict()), 200
    else:
        return jsonify({'error': 'Amenity not found'}), 404

@amenity_bp.route('/<int:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    amenity = data_manager.get_amenity_by_id(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    amenity.name = name
    data_manager.update_amenity(amenity)

    return jsonify(amenity.to_dict()), 200

@amenity_bp.route('/<int:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = data_manager.get_amenity_by_id(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    data_manager.delete_amenity(amenity_id)
    return jsonify(), 204

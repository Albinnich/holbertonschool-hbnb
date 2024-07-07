from datetime import datetime
from flask import Blueprint, jsonify, request

from models.amenity import Amenity
from Repository.amenity_repository import AmenityRepository


amenity_controller = Blueprint('amenity_controller', __name__)

amenity_manager = AmenityRepository()

@amenity_controller.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    name = data.get("name")
    amenity = Amenity(name)
    valid, msg = amenity_manager.create_amenity(amenity)
    if not valid:
        return jsonify({"message": "Amenity not created", "error": msg})  
    return jsonify(amenity.__dict__)


@amenity_controller.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = amenity_manager.get_amenities()
    return jsonify(amenities)


@amenity_controller.route('/amenities/<amenity_id>', methods=['GET'])
def get_specific(amenity_id):
    valid, msg = amenity_manager.get_amenity_details(amenity_id)
    if not valid:
        return jsonify({"message": "Amenity not found", "error": msg})
    return jsonify(msg)


@amenity_controller.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenities(amenity_id):
    valid, old_data = amenity_manager.get_amenity_details(amenity_id)
    if not valid:
        msg = old_data
        return jsonify({"message": "Amenity not updated", "error": msg})
    data = request.get_json()
    name = data.get("name")
    
    amenity = Amenity(name)
    amenity.id = amenity_id
    amenity.created_at = old_data["created_at"]
    amenity.updated_at = datetime.now().isoformat()
    valid, msg = amenity_manager.update_amenity(amenity_id, amenity)
    if not valid:
        return jsonify({"message": "Amenity not updated", "error": msg})
    return jsonify(amenity.__dict__)

@amenity_controller.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenities(amenity_id):
    valid, msg = amenity_manager.delete_amenity(amenity_id)
    if not valid:
        return jsonify({"message": "Amenity not deleted", "error": msg})
    return jsonify({"message": "Amenity deleted successfully"})
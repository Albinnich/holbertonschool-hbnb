from datetime import datetime
from flask import Blueprint, jsonify, request

from Model.place import Place
from Repository.place_repository import PlaceRepository


place_controller = Blueprint('place_controller', __name__)

place_manager = PlaceRepository()

@place_controller.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    address = data.get('address')
    city_id = data.get('city_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host_id = data.get('host_id')
    number_of_rooms = data.get('number_of_rooms')
    number_of_bathrooms = data.get('number_of_bathrooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    amenity_ids = data.get('amenity_ids')
    place = Place(name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids)
    valid, msg = place_manager.create_place(place)
    if not valid:
        return jsonify({"message": "Place not created", "error": msg})
    return jsonify(place.__dict__)


@place_controller.route('/places', methods=['GET'])
def get_places():
    places = place_manager.get_all_places()
    return jsonify(places)


@place_controller.route('/places/<place_id>', methods=['GET'])
def get_specific(place_id):
    valid, msg = place_manager.get_place_details(place_id)
    if not valid:
        return jsonify({"message": "Place not found", "error": msg})
    return jsonify(msg)


@place_controller.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    valid, old_data = place_manager.get_place_details(place_id)
    if not valid:
        msg = old_data
        return jsonify({"message": "Place not updated", "error": msg})
    data = request.get_json()
    name = data['name']
    description = data.get('description')
    address = data.get('address')
    city_id = data.get('city_id')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host_id = data.get('host_id')
    number_of_rooms = data.get('number_of_rooms')
    number_of_bathrooms = data.get('number_of_bathrooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    amenity_ids = data.get('amenity_ids')
    
    place = Place(name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids)
    place.id = place_id
    place.created_at = old_data["created_at"]
    place.updated_at = datetime.now().isoformat()
    valid, msg = place_manager.update_place(place_id, place)
    if not valid:
        return jsonify({"message": "Place not updated", "error": msg})
    return jsonify(place.__dict__)


@place_controller.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    valid, msg = place_manager.delete_place(place_id)
    if not valid:
        return jsonify({"message": "Place not deleted", "error": msg})
    return jsonify({"message": "Place deleted successfully"})
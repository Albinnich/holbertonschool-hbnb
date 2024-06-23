from flask import Blueprint, jsonify, request
from models.city import City
from models.country import Country
from data_manager import DataManager

city_routes = Blueprint('city_routes', __name__)
data_manager = DataManager()

@city_routes.route('/cities', methods=['POST'])
def create_city():
    data = request.json
    name = data.get('name')
    country_code = data.get('country_code')

    if not name or not country_code:
        return jsonify({'error': 'Name and country_code are required'}), 400

    country = data_manager.get_country_by_code(country_code)
    if not country:
        return jsonify({'error': 'Invalid country_code'}), 400

    existing_city = data_manager.get_city_by_name_and_country(name, country_code)
    if existing_city:
        return jsonify({'error': 'City already exists in this country'}), 409

    city = City(name=name, country_code=country_code)
    data_manager.save_city(city)
    return jsonify(city.to_dict()), 201

@city_routes.route('/cities', methods=['GET'])
def get_cities():
    cities = data_manager.get_cities()
    return jsonify([city.to_dict() for city in cities])

@city_routes.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = data_manager.get_city_by_id(city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        return jsonify({'error': 'City not found'}), 404

@city_routes.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.json
    name = data.get('name')
    country_code = data.get('country_code')

    city = data_manager.get_city_by_id(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    if name:
        city.name = name
    if country_code:
        country = data_manager.get_country_by_code(country_code)
        if not country:
            return jsonify({'error': 'Invalid country_code'}), 400
        city.country_code = country_code

    data_manager.update_city(city)
    return jsonify(city.to_dict()), 200

@city_routes.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = data_manager.get_city_by_id(city_id)
    if city:
        data_manager.delete_city(city_id)
        return '', 204
    else:
        return jsonify({'error': 'City not found'}), 404


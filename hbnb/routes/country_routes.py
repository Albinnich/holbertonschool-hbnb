from flask import Blueprint, jsonify, request
from models.country import Country
from data_manager import DataManager

country_routes = Blueprint('country_routes', __name__)
data_manager = DataManager()

@country_routes.route('/countries', methods=['GET'])
def get_countries():
    countries = data_manager.get_countries()
    return jsonify([country.to_dict() for country in countries])

@country_routes.route('/countries/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country = data_manager.get_country_by_code(country_code)
    if country:
        return jsonify(country.to_dict())
    else:
        return jsonify({'error': 'Country not found'}), 404

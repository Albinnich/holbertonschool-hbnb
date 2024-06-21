from flask import Blueprint
from flask_restx import Api
from .amenities import ns as amenities_namespace

api_bp = Blueprint('api', __name__)

api = Api(api_bp, version='1.0', title='Amenity API',
          description='A simple Amenity API')

api.add_namespace(amenities_namespace, path='/amenities')

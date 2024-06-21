# app/__init__.py
from flask import Flask
from flask_restx import Api
from app.routes.amenities import ns as amenities_namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='Amenity API', description='A simple Amenity API')
api.add_namespace(amenities_namespace, path='/amenities')

if __name__ == '__main__':
    app.run(debug=True)

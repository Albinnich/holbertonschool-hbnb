from flask import Flask
from app.routes.user_routes import user_bp
from routes.country_routes import country_routes
from routes.city_routes import city_routes

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(country_routes, url_prefix='/api')
    app.register_blueprint(city_routes, url_prefix='/api')

    return app

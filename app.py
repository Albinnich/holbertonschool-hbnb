import flask
from Api.user_controller import user_controller
from Api.city_controller import city_controller
from Api.amenity_controller import amenity_controller
from Api.place_controller import place_controller
from Api.review_controller import review_controller

app = flask.Flask(__name__)

app.register_blueprint(user_controller)
app.register_blueprint(city_controller)
app.register_blueprint(amenity_controller)
app.register_blueprint(place_controller)
app.register_blueprint(review_controller)

@app.route('/', methods=['GET'])
def index():
    return "Hello"

app.run("0.0.0.0", port=5000, debug=True)
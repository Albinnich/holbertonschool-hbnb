# review_routes.py

from flask import Blueprint, request, jsonify
from models.review import Review
from data_manager import DataManager

review_bp = Blueprint('review', __name__, url_prefix='/reviews')
data_manager = DataManager()

@review_bp.route('/places/<int:place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.json
    required_fields = ['user_id', 'rating', 'comment']

    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400

    # Validate rating
    rating = data.get('rating')
    if not isinstance(rating, int) or rating < 1 or rating > 5:
        return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

    # Validate user_id and place_id
    user_id = data.get('user_id')
    if not data_manager.get_user_by_id(user_id):
        return jsonify({'error': 'Invalid user_id'}), 400

    if not data_manager.get_place_by_id(place_id):
        return jsonify({'error': 'Invalid place_id'}), 400

    # Ensure user is not reviewing their own place (based on host_id comparison or similar logic)
    place = data_manager.get_place_by_id(place_id)
    if place.host_id == user_id:
        return jsonify({'error': 'Hosts cannot review their own place'}), 400

    new_review = Review(place_id=place_id, **data)
    data_manager.save_review(new_review)

    return jsonify(new_review.to_dict()), 201

@review_bp.route('/users/<int:user_id>/reviews', methods=['GET'])
def get_reviews_by_user(user_id):
    reviews = data_manager.get_reviews_by_user(user_id)
    return jsonify([review.to_dict() for review in reviews]), 200

@review_bp.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    reviews = data_manager.get_reviews_by_place(place_id)
    return jsonify([review.to_dict() for review in reviews]), 200

@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = data_manager.get_review_by_id(review_id)
    if review:
        return jsonify(review.to_dict()), 200
    else:
        return jsonify({'error': 'Review not found'}), 404

@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    review = data_manager.get_review_by_id(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    # Validate rating if present
    rating = data.get('rating')
    if rating and (not isinstance(rating, int) or rating < 1 or rating > 5):
        return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

    # Validate user_id and place_id if present
    if 'user_id' in data and not data_manager.get_user_by_id(data['user_id']):
        return jsonify({'error': 'Invalid user_id'}), 400

    if 'place_id' in data and not data_manager.get_place_by_id(data['place_id']):
        return jsonify({'error': 'Invalid place_id'}), 400

    # Ensure user is not updating their review to review their own place (based on host_id comparison or similar logic)
    if 'place_id' in data:
        place = data_manager.get_place_by_id(data['place_id'])
        if place.host_id == data['user_id']:
            return jsonify({'error': 'Hosts cannot review their own place'}), 400

    # Update review fields
    for key, value in data.items():
        setattr(review, key, value)

    data_manager.update_review(review)

    return jsonify(review.to_dict()), 200

@review_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = data_manager.get_review_by_id(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    data_manager.delete_review(review_id)
    return jsonify(), 204


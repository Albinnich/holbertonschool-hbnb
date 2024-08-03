from datetime import datetime
from flask import Blueprint, jsonify, request

from Model.review import Review
from Repository.review_repository import ReviewRepository


review_controller = Blueprint('review_controller', __name__)

review_manager = ReviewRepository()


@review_controller.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    data = request.get_json()
    user_id = data.get('user_id')
    rating = data.get('rating')
    comment = data.get('comment')
    review = Review(place_id, user_id, rating, comment)
    valid, msg, status_code = review_manager.create_new_review(review)
    if not valid:
        return jsonify({"message": "Review not created", "error": msg}), status_code
    return jsonify(review.__dict__), 201


@review_controller.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    valid, msg, status_code = review_manager.get_place_reviews(place_id)
    if not valid:
        return jsonify({"message": "Reviews not found", "error": msg}), status_code
    reviews = msg
    return jsonify(reviews), 200


@review_controller.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    valid, msg, status_code = review_manager.get_user_reviews(user_id)
    if not valid:
        return jsonify({"message": "Reviews not found", "error": msg}), status_code
    reviews = msg
    return jsonify(reviews), 200


@review_controller.route('/reviews/<review_id>', methods=['GET'])
def get_specific(review_id):
    valid, msg, status_code = review_manager.get_review_details(review_id)
    if not valid:
        return jsonify({"message": "Review not found", "error": msg}), status_code
    return jsonify(msg), 200


@review_controller.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    valid, old_data, status_code = review_manager.get_review_details(review_id)
    if not valid:
        msg = old_data
        return jsonify({"message": "Review not updated", "error": msg}), status_code
    data = request.get_json()
    rating = data.get('rating')
    comment = data.get('comment')
    review = Review(old_data["place_id"], old_data["user_id"], rating, comment)
    review.id = review_id
    review.created_at = old_data["created_at"]
    review.updated_at = datetime.now().isoformat()
    valid, msg, status_code = review_manager.update_review(review_id, review)
    if not valid:
        return jsonify({"message": "Review not updated", "error": msg}), status_code
    return jsonify(review.__dict__), 200


@review_controller.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    valid, msg, status_code = review_manager.delete_review(review_id)
    if not valid:
        return jsonify({"message": "Review not deleted", "error": msg}), status_code
    return jsonify({"message": "Review deleted"}), 200
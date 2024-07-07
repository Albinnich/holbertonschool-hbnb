from datetime import datetime
from flask import Blueprint, jsonify, request

from models.user import User
from Repository.user_repository import UserRepository


user_controller = Blueprint('user_controller', __name__)

user_manager = UserRepository()

@user_controller.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    user = User(email, first_name, last_name)
    valid, msg, status_code = user_manager.create_user(user)
    if not valid:
        return jsonify({"message": "User not created", "error": msg}), status_code
    return jsonify(user.__dict__), 201
    

@user_controller.route('/users', methods=['GET'])
def get_users():
    users = user_manager.get_users()
    return jsonify(users), 200


@user_controller.route('/users/<user_id>', methods=['GET'])
def get_specific(user_id):
    valid, msg, status_code = user_manager.get_user_details(user_id)
    if not valid:
        return jsonify({"message": "User not found", "error": msg}), status_code
    user = msg
    return jsonify(user), 200


@user_controller.route('/users/<user_id>', methods=['PUT'])
def update_users(user_id):
    valid, old_data, status_code = user_manager.get_user_details(user_id)
    if not valid:
        msg = old_data
        return jsonify({"message": "User not updated", "error": msg}), status_code
    data = request.get_json()
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    user = User(email, first_name, last_name)
    user.id = user_id
    user.created_at = old_data["created_at"]
    user.updated_at = datetime.now().isoformat()
    valid, msg, status_code = user_manager.update_user(user_id, user)
    if not valid:
        return jsonify({"message": "User not updated", "error": msg}), status_code
    return jsonify(user.__dict__), 200


@user_controller.route('/users/<user_id>', methods=['DELETE'])
def delete_users(user_id):
    valid, msg, status_code = user_manager.delete_user(user_id)
    if not valid:
        return jsonify({"message": "User not deleted", "error": msg}), status_code
    return jsonify({"message": "User deleted successfully"}), 200
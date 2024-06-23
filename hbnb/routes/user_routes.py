from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound, Conflict
from datetime import datetime
from app.models.user import User
from app.persistence.data_manager import DataManager

user_bp = Blueprint('user', __name__)
data_manager = DataManager()

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data:
        raise BadRequest('No data provided')

    try:
        # Validate required fields
        required_fields = ['email', 'password', 'first_name', 'last_name']
        for field in required_fields:
            if field not in data:
                raise BadRequest(f'Missing required field: {field}')
        
        # Check if email already exists
        existing_user = data_manager.get_user_by_email(data['email'])
        if existing_user:
            raise Conflict(f'User with email {data["email"]} already exists')

        # Create new user object
        new_user = User(
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        # Save user to data manager
        data_manager.save_user(new_user)

        return jsonify(new_user.to_dict()), 201
    
    except ValueError as e:
        raise BadRequest(str(e))

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = data_manager.get_all_users()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get_user(user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        raise NotFound('User not found')

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    try:
        existing_user = data_manager.get_user(user_id)
        if not existing_user:
            raise NotFound('User not found')

        if 'email' in data:
            # Check if new email already exists
            new_email = data['email']
            if new_email != existing_user.email:
                check_user = data_manager.get_user_by_email(new_email)
                if check_user:
                    raise Conflict(f'User with email {new_email} already exists')

            existing_user.email = new_email

        if 'password' in data:
            existing_user.password = data['password']

        if 'first_name' in data:
            existing_user.first_name = data['first_name']

        if 'last_name' in data:
            existing_user.last_name = data['last_name']

        existing_user.updated_at = datetime.utcnow()

        data_manager.update_user(existing_user)
        return jsonify(existing_user.to_dict())
    
    except ValueError as e:
        raise BadRequest(str(e))

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        data_manager.delete_user(user_id)
        return '', 204
    except ValueError as e:
        raise BadRequest(str(e))

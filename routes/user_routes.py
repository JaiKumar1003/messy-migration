from flask import Blueprint, request, jsonify
from services.user_service import (
    get_all_users, get_user_by_id, create_user,
    update_user, delete_user, search_users, login_user
)

user_bp = Blueprint('user_routes', __name__)

@user_bp.route('/')
def home():
    return "User Management System"

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users), 200

@user_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    success, message = create_user(data)
    status = 201 if success else 400
    return jsonify({"message": message}), status

@user_bp.route('/user/<user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    success, message = update_user(user_id, data)
    status = 200 if success else 400
    return jsonify({"message": message}), status

@user_bp.route('/user/<user_id>', methods=['DELETE'])
def delete(user_id):
    success, message = delete_user(user_id)
    status = 200 if success else 404
    return jsonify({"message": message}), status

@user_bp.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    users = search_users(name)
    return jsonify(users), 200

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = login_user(data)
    return jsonify(result), 200

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.services.user_service import UserService
from app.exceptions.errors import ValidationError

auth_bp = Blueprint('auth', __name__)

service = UserService()

@auth_bp.route('/register', methods=['POST'])
def register():

    data = request.get_json()

    if not isinstance(data, dict):
        raise ValidationError('Request body must contain valid JSON.')

    username = data['username']
    password = data['password']

    user = service.register(username, password)

    return jsonify({
        "message": "User registered successfully",
        "username": user.username,
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    if not isinstance(data, dict):
        raise ValidationError('Request body must contain valid JSON.')

    username = data['username']
    password = data['password']

    user = service.repository.get_by_username(username)

    token = service.login(username, password)

    return jsonify({
        "message": "Logged in successfully",
        "access_token": token,
    })
#--------------------------------------------
# DEPENDENCIES
#--------------------------------------------
import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, logout_user

#--------------------------------------------
# CREATE BLUEPRINT
#--------------------------------------------
users = Blueprint('users','users')

#--------------------------------------------
# GET USERS
#--------------------------------------------
@users.route('/', methods=['GET'])
def users_index():
    result = models.User.select()
    user_dicts = [model_to_dict(user) for user in result]
    return jsonify({
        'data': user_dicts,
        'message': f"Successfully found {len(user_dicts)} users",
        'status': 200
    }), 200

#--------------------------------------------
# REGISTER USER
#--------------------------------------------
@users.route('/register/', methods=['POST'])
def register():
# GET INPUT
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()
# IS EMAIL ADDRESS ALREADY REGISTERED?
    try:
        print('is email already registered?')
        models.User.get(models.User.email == payload['email'])
        return jsonify(
            data={},
            message=f"A user with email {payload['email']} already exists",
            status=401
        ), 401
    except models.DoesNotExist:
# IS USERNAME ALREADY REGISTERED?
        try:
            print('does username exist?')
            models.User.get(models.User.username == payload['username'])
            return jsonify(
                data={},
                message=f"A user with username {payload['username']} already exists",
                status=401
            ), 401
# CREATE & LOGIN NEW USER
        except:
            pw_hash = generate_password_hash(payload['password'])
            created_user = models.User.create(
                username=payload['username'],
                email=payload['email'],
                password=pw_hash
            )
            login_user(created_user)
            created_user_dict = model_to_dict(created_user)
            created_user_dict.pop('password')
            return jsonify(
                data=created_user_dict,
                message=f"Successfully registered user {created_user_dict['email']}",
                status=201
            ), 201

#--------------------------------------------
# LOGIN EXISTING USER
#--------------------------------------------
@users.route('/login', methods=['POST'])
def login():
    print('login route!')
    payload = request.get_json()
    print(payload)
    payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()
# IS EMAIL ADDRESS A REGISTERED USER?
    try:
        user = models.User.get(models.User.email == payload['email'])
        user_dict = model_to_dict(user)
# IS PASSWORD CORRECT FOR USER?
        password_is_good = check_password_hash(user_dict['password'], payload['password'])
        if (password_is_good):
# LOGIN VALIDATED USER
            login_user(user)
            user_dict.pop('password')
            return jsonify(
                data=user_dict,
                message=f"Successfully logged in {user_dict['email']}",
                status=200
            ), 200
# RETURN ERROR MESSAGE FOR INCORRECT PASSWORD
        else:
            return jsonify(
                data={},
                message='Email or password is incorrect',
                status = 401
            ), 401
# RETURN ERROR MESSAGE FOR USER DOES NOT EXIST
    except models.DoesNotExist:
        return jsonify(
            data={},
            message="Email or password is incorrect",
            status=401
        ), 401

#--------------------------------------------
# LOGOUT CURRENT USER
#--------------------------------------------
@users.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return jsonify(
        data={},
        status=200,
        message='User successfully logged out'
    ), 200

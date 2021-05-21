#--------------------------------------------
# DEPENDENCIES
#--------------------------------------------
import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, logout_user, current_user


#--------------------------------------------
# CREATE BLUEPRINT
#--------------------------------------------
userexercises = Blueprint('userexercises','userexercises')

#--------------------------------------------
# GET USER EXERCISES
#--------------------------------------------
@userexercises.route('/', methods=['GET'])
def userexercises_index():
    result = current_user.this_users_exercises
    userexercises_dicts = [model_to_dict(userexercises) for userexercises in result]
    return jsonify({
        'data': userexercises_dicts,
        'message': f"Successfully found {len(userexercises_dicts)} user exercises",
        'status': 200
    }), 200

#--------------------------------------------
# ADD EXERCISE TO USER
#--------------------------------------------
@userexercises.route('/add/<exercise_id>', methods=['POST'])
def add(exercise_id):
# GET INPUT
    payload = request.get_json()
    # MAY WANT TO ADD IF USEREXERCISE DOES NOT ALREADY EXIST, CREATE, ELSE RETURN ERROR MESSAGE
    new_exercise = models.UserExercise.create(
    user= current_user.id,
    exercise = exercise_id,
    completed = payload['completed'],
    completed_count = payload['completed_count'],
    favorite = payload['favorite'],
    recommended = payload['recommended']
    )
    user_exercise_dict = model_to_dict(new_exercise)
    return jsonify(
        data=user_exercise_dict,
        message='Successfully add exercise to user!',
        status=201
    ), 201

#--------------------------------------------
# SHOW USER EXERCISE
#--------------------------------------------
@userexercises.route('/<user_exercise_id>', methods=["GET"])
def get_one_user_exercise(user_exercise_id):
    user_exercise = models.UserExercise.get_by_id(user_exercise_id)
    return jsonify(
    data = model_to_dict(user_exercise),
    message = 'Success!!',
    status = 200
    ), 200


#--------------------------------------------
# UPDATE USER EXERCISE
#--------------------------------------------
@userexercises.route('/<user_exercise_id>', methods=["PUT"])
def update_user_exercise(user_exercise_id):
    payload = request.get_json()
    models.UserExercise.update(**payload).where(models.UserExercise.id==user_exercise_id).execute()
    return jsonify(
        data = model_to_dict(models.UserExercise.get_by_id(user_exercise_id)),
        status = 200,
        message = 'resource updated successfully'
    ), 200

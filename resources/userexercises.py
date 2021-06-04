#--------------------------------------------
# DEPENDENCIES
#--------------------------------------------
import models
from peewee import *
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
@userexercises.route('/', methods=['POST'])
def addUserExercise():
# GET INPUT

    payload = request.get_json()

    user_exercise, created = models.UserExercise.get_or_create(
        exercise=payload["exercise"],
        user=current_user.id,
        defaults={
            "exercise" : payload['exercise'],
            "completed" : payload['completed'],
            "completed_count" : payload['completed_count'],
            "favorite" : payload['favorite'],
            "recommended" : payload['recommended']
        }
    )
    user_exercise_dict = model_to_dict(user_exercise)
    if (created):
        return jsonify(
            data=user_exercise_dict,
            message='User exercise was added!',
            status=201
        ), 201
    else:
        return jsonify(
            data=user_exercise_dict,
            message="User already existed",
            status=200
        )

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

#--------------------------------------------
# DELETE USER EXERCISE
#--------------------------------------------
@userexercises.route('/<user_exercise_id>', methods=["DELETE"])
def delete_user_exercise(user_exercise_id):
    models.UserExercise.delete().where(models.UserExercise.id==user_exercise_id).execute()
    return jsonify(
        data = None,
        status = 200,
        message = 'resource deleted successfully'
    )

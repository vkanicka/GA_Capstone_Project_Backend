#--------------------------------------------
# IMPORTS
#--------------------------------------------
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user#, login_required

#--------------------------------------------
# CREATE BLUEPRINT
#--------------------------------------------
exercises = Blueprint('exercises', 'exercises')

#--------------------------------------------
# GET EXERCISES
#--------------------------------------------
@exercises.route('/', methods=['GET'])
def exercises_index():
    result = models.Exercise.select()
    exercise_dicts = [model_to_dict(exercise) for exercise in result]
    return jsonify({
        'data': exercise_dicts,
        'message': f"Successfully found {len(exercise_dicts)} exercises",
        'status': 200
    }), 200

#--------------------------------------------
# CREATE EXERCISE
#--------------------------------------------
@exercises.route('/', methods=['POST'])
# @login_required
def create_exercise():
    payload = request.get_json()
    new_exercise = models.Exercise.create(**payload)
    exercise_dict = model_to_dict(new_exercise)
    return jsonify(
        data=exercise_dict,
        message='Successfully created exercise!',
        status=201
    ), 201

#--------------------------------------------
# SHOW EXERCISE
#--------------------------------------------
@exercises.route('/<id>', methods=["GET"])
def get_one_exercise(id):
    exercise = models.Exercise.get_by_id(id)
    return jsonify(
    data = model_to_dict(exercise),
    message = 'Success!!',
    status = 200
    ), 200

#--------------------------------------------
# UPDATE EXERCISE
#--------------------------------------------
@exercises.route('/<id>', methods=["PUT"])
def update_exercise(id):
    payload = request.get_json()
    models.Exercise.update(**payload).where(models.Exercise.id==id).execute()
    return jsonify(
        data = model_to_dict(models.Exercise.get_by_id(id)),
        status = 200,
        message = 'resource updated successfully'
    ), 200

#--------------------------------------------
# DELETE EXERCISE
#--------------------------------------------
@exercises.route('/<id>', methods=["DELETE"])
def delete_exercise(id):
    models.Exercise.delete().where(models.Exercise.id==id).execute()
    return jsonify(
        data = None,
        status = 200,
        message = 'resource deleted successfully'
    )

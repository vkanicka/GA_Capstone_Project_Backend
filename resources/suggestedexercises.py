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
suggestedexercises = Blueprint('suggestedexercises', 'suggestedexercises')

#--------------------------------------------
# GET SUGGESTEDEXERCISES
#--------------------------------------------
@suggestedexercises.route('/', methods=['GET'])
def suggestedexercises_index():
    result = models.SuggestedExercise.select()
    suggestedexercise_dicts = [model_to_dict(suggestedexercise) for suggestedexercise in result]
    return jsonify({
        'data': suggestedexercise_dicts,
        'message': f"Successfully found {len(suggestedexercise_dicts)} suggestedexercises",
        'status': 200
    }), 200

#--------------------------------------------
# CREATE SUGGESTEDEXERCISE
#--------------------------------------------
@suggestedexercises.route('/', methods=['POST'])
# @login_required
def create_suggestedexercise():
    payload = request.get_json()
    new_suggestedexercise = models.SuggestedExercise.create(**payload)
    suggestedexercise_dict = model_to_dict(new_suggestedexercise)
    return jsonify(
        data=suggestedexercise_dict,
        message='Successfully created suggestedexercise!',
        status=201
    ), 201

#--------------------------------------------
# SHOW SUGGESTEDEXERCISE
#--------------------------------------------
@suggestedexercises.route('/<id>', methods=["GET"])
def get_one_suggestedexercise(id):
    suggestedexercise = models.SuggestedExercise.get_by_id(id)
    return jsonify(
    data = model_to_dict(suggestedexercise),
    message = 'Success!!',
    status = 200
    ), 200

#--------------------------------------------
# UPDATE SUGGESTEDEXERCISE
#--------------------------------------------
@suggestedexercises.route('/<id>', methods=["PUT"])
def update_suggestedexercise(id):
    payload = request.get_json()
    models.SuggestedExercise.update(**payload).where(models.SuggestedExercise.id==id).execute()
    return jsonify(
        data = model_to_dict(models.SuggestedExercise.get_by_id(id)),
        status = 200,
        message = 'resource updated successfully'
    ), 200

#--------------------------------------------
# DELETE SUGGESTEDEXERCISE
#--------------------------------------------
@suggestedexercises.route('/<id>', methods=["DELETE"])
def delete_suggestedexercise(id):
    models.SuggestedExercise.delete().where(models.SuggestedExercise.id==id).execute()
    return jsonify(
        data = None,
        status = 200,
        message = 'resource deleted successfully'
    )

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
inputformstest = Blueprint('inputformstest', 'inputformstest')

#--------------------------------------------
# GET EXERCISES
#--------------------------------------------
@inputformstest.route('/', methods=['GET'])
def inputforms_index():
    result = models.InputFormTest.select()
    input_form_dicts = [model_to_dict(input_form) for input_form in result]
    return jsonify({
        'data': input_form_dicts,
        'message': f"Successfully found {len(input_form_dicts)} inputforms",
        'status': 200
    }), 200

#--------------------------------------------
# CREATE EXERCISE
#--------------------------------------------
@inputformstest.route('/', methods=['POST'])
# @login_required
def create_input_form():
    payload = request.get_json()
    print(payload)
    new_input_form = models.InputFormTest.create(
    user=current_user.id
    )
    input_form_dict = model_to_dict(new_input_form)
    return jsonify(
        data=input_form_dict,
        message='Successfully created input_form!',
        status=201
    ), 201
# def create_input_etbs():
#     payload = request.get_json()
#     new_emotions = models.Emotion.create()
#--------------------------------------------
# SHOW EXERCISE
#--------------------------------------------
@inputformstest.route('/<id>', methods=["GET"])
def get_one_input_form(id):
    input_form = models.InputFormTest.get_by_id(id)
    return jsonify(
    data = model_to_dict(input_form),
    message = 'Success!!',
    status = 200
    ), 200

#--------------------------------------------
# UPDATE EXERCISE
#--------------------------------------------
@inputformstest.route('/<id>', methods=["PUT"])
def update_input_form(id):
    payload = request.get_json()
    models.InputFormTest.update(**payload).where(models.InputFormTest.id==id).execute()
    return jsonify(
        data = model_to_dict(models.InputFormTest.get_by_id(id)),
        status = 200,
        message = 'resource updated successfully'
    ), 200

#--------------------------------------------
# DELETE EXERCISE
#--------------------------------------------
@inputformstest.route('/<id>', methods=["DELETE"])
def delete_input_form(id):
    models.InputFormTest.delete().where(models.InputFormTest.id==id).execute()
    return jsonify(
        data = None,
        status = 200,
        message = 'resource deleted successfully'
    )

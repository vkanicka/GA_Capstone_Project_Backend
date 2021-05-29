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
behavior = Blueprint('behavior', 'behavior')

#--------------------------------------------
# GET BEHAVIORS
#--------------------------------------------
@behavior.route('/', methods=['GET'])
def behavior_index():
    result = models.Behavior.select()
    behavior_dicts = [model_to_dict(behavior) for behavior in result]
    return jsonify({
        'data': behavior_dicts,
        'message': f"Successfully found {len(behavior_dicts)} behavior",
        'status': 200
    }), 200

#--------------------------------------------
# CREATE BEHAVIOR
#--------------------------------------------
@behavior.route('/', methods=['POST'])
# @login_required
def create_behavior():
    payload = request.get_json()
    new_behavior = models.Behavior.create(**payload)
    behavior_dict = model_to_dict(new_behavior)
    return jsonify(
        data=behavior_dict,
        message='Successfully created behavior!',
        status=201
    ), 201

#--------------------------------------------
# SHOW BEHAVIOR
#--------------------------------------------
@behavior.route('/<id>', methods=["GET"])
def get_one_behavior(id):
    behavior = models.Behavior.get_by_id(id)
    return jsonify(
    data = model_to_dict(behavior),
    message = 'Success!!',
    status = 200
    ), 200

#--------------------------------------------
# UPDATE BEHAVIOR
#--------------------------------------------
@behavior.route('/<id>', methods=["PUT"])
def update_behavior(id):
    payload = request.get_json()
    models.Behavior.update(**payload).where(models.Behavior.id==id).execute()
    return jsonify(
        data = model_to_dict(models.Behavior.get_by_id(id)),
        status = 200,
        message = 'resource updated successfully'
    ), 200

#--------------------------------------------
# DELETE BEHAVIOR
#--------------------------------------------
@behavior.route('/<id>', methods=["DELETE"])
def delete_behavior(id):
    models.Behavior.delete().where(models.Behavior.id==id).execute()
    return jsonify(
        data = None,
        status = 200,
        message = 'resource deleted successfully'
    )

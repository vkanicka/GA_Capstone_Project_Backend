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
thought = Blueprint('thought', 'thought')

#--------------------------------------------
# GET THOUGHTS
#--------------------------------------------
@thought.route('/', methods=['GET'])
def thought_index():
    result = models.Thought.select()
    thought_dicts = [model_to_dict(thought) for thought in result]
    return jsonify({
        'data': thought_dicts,
        'message': f"Successfully found {len(thought_dicts)} thought",
        'status': 200
    }), 200

#--------------------------------------------
# CREATE THOUGHT
#--------------------------------------------
@thought.route('/', methods=['POST'])
# @login_required
def create_thought():
    payload = request.get_json()
    new_thought = models.Thought.create(**payload)
    thought_dict = model_to_dict(new_thought)
    return jsonify(
        data=thought_dict,
        message='Successfully created thought!',
        status=201
    ), 201

#--------------------------------------------
# SHOW THOUGHT
#--------------------------------------------
@thought.route('/<id>', methods=["GET"])
def get_one_thought(id):
    thought = models.Thought.get_by_id(id)
    return jsonify(
    data = model_to_dict(thought),
    message = 'Success!!',
    status = 200
    ), 200

#--------------------------------------------
# UPDATE THOUGHT
#--------------------------------------------
@thought.route('/<id>', methods=["PUT"])
def update_thought(id):
    payload = request.get_json()
    models.Thought.update(**payload).where(models.Thought.id==id).execute()
    return jsonify(
        data = model_to_dict(models.Thought.get_by_id(id)),
        status = 200,
        message = 'resource updated successfully'
    ), 200

#--------------------------------------------
# DELETE THOUGHT
#--------------------------------------------
@thought.route('/<id>', methods=["DELETE"])
def delete_thought(id):
    models.Thought.delete().where(models.Thought.id==id).execute()
    return jsonify(
        data = None,
        status = 200,
        message = 'resource deleted successfully'
    )

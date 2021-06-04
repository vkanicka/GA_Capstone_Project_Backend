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
emotion = Blueprint('emotion', 'emotion')

#--------------------------------------------
# GET EMOTIONS
#--------------------------------------------
@emotion.route('/', methods=['GET'])
def emotion_index():
    result = models.Emotion.select().order_by(Emotion.id)
    emotion_dicts = [model_to_dict(emotion) for emotion in result]
    return jsonify({
        'data': emotion_dicts,
        'message': f"Successfully found {len(emotion_dicts)} emotion",
        'status': 200
    }), 200

#--------------------------------------------
# CREATE EMOTION
#--------------------------------------------
@emotion.route('/', methods=['POST'])
# @login_required
def create_emotion():
    payload = request.get_json()
    new_emotion = models.Emotion.create(**payload)
    emotion_dict = model_to_dict(new_emotion)
    return jsonify(
        data=emotion_dict,
        message='Successfully created emotion!',
        status=201
    ), 201

#--------------------------------------------
# SHOW EMOTION
#--------------------------------------------
@emotion.route('/<id>', methods=["GET"])
def get_one_emotion(id):
    emotion = models.Emotion.get_by_id(id)
    return jsonify(
    data = model_to_dict(emotion),
    message = 'Success!!',
    status = 200
    ), 200

#--------------------------------------------
# UPDATE EMOTION
#--------------------------------------------
@emotion.route('/<id>', methods=["PUT"])
def update_emotion(id):
    payload = request.get_json()
    models.Emotion.update(**payload).where(models.Emotion.id==id).execute()
    return jsonify(
        data = model_to_dict(models.Emotion.get_by_id(id)),
        status = 200,
        message = 'resource updated successfully'
    ), 200

#--------------------------------------------
# DELETE EMOTION
#--------------------------------------------
@emotion.route('/<id>', methods=["DELETE"])
def delete_emotion(id):
    models.Emotion.delete().where(models.Emotion.id==id).execute()
    return jsonify(
        data = None,
        status = 200,
        message = 'resource deleted successfully'
    )

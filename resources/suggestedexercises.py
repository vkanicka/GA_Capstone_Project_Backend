#--------------------------------------------
# IMPORTS
#--------------------------------------------
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user#, login_required
import os
from playhouse.db_url import connect

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
    # from the_query import clearSuggestedExerciseTable
    # clearSuggestedExerciseTable()
    # from the_query import suggestExercise


    emotions = (models.Emotion
         .select(
         models.Emotion, models.EmotionTags, models.Tag)
         .join(models.EmotionTags, on=(models.Emotion.id==models.EmotionTags.emotion_id))
         .join(models.Tag, on=(models.EmotionTags.tag_id==models.Tag.id))
         .where(models.Emotion.status==True)
         )

    for emotion in emotions:
        print('emo')
        print(emotion.emotion, emotion.id, emotion.emotiontags.emotion_id, emotion.emotiontags.tag_id, emotion.emotiontags.tag.id,
        emotion.emotiontags.tag.tag
        )

    thoughts = (models.Thought
         .select(
         models.Thought, models.ThoughtTags, models.Tag)
         .join(models.ThoughtTags, on=(models.Thought.id==models.ThoughtTags.thought_id))
         .join(models.Tag, on=(models.ThoughtTags.tag_id==models.Tag.id))
         .where(models.Thought.status==True)
         )

    for thought in thoughts:
        print('thought')
        print(thought.thought, thought.id, thought.thoughttags.thought_id, thought.thoughttags.tag_id, thought.thoughttags.tag.id,
        thought.thoughttags.tag.tag
        )

    behaviors = (models.Behavior
         .select(
         models.Behavior, models.BehaviorTags, models.Tag)
         .join(models.BehaviorTags, on=(models.Behavior.id==models.BehaviorTags.behavior_id))
         .join(models.Tag, on=(models.BehaviorTags.tag_id==models.Tag.id))
         .where(models.Behavior.status==True)
         )

    for behavior in behaviors:
        print('behavior')
        print(behavior.behavior, behavior.id, behavior.behaviortags.behavior_id, behavior.behaviortags.tag_id, behavior.behaviortags.tag.id,
        behavior.behaviortags.tag.tag
        )


    def queryPSQL():
        return models.Emotion.select(models.Emotion).where(models.Emotion.status==True).execute() # this returns the first emotion ID selected

    payload = queryPSQL()
    for i in payload:
        print('EMOTION ID SELECTED: '+str(i))
    #
    # payload = suggestExercise()
    new_suggestedexercise = models.SuggestedExercise.create(exercise = payload[0])
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

#--------------------------------------------
# IMPORTS
#--------------------------------------------
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user#, login_required
import os
from playhouse.db_url import connect
import pandas as pd
from peewee import *
from peewee import fn

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
    models.SuggestedExercise.truncate_table(restart_identity=True)


    emotions = (models.Emotion
         .select(
           models.Tag.id.alias("tag_id")
         , fn.Count(models.Tag.id).alias("count")
         )
         .join(models.EmotionTags, on=(models.Emotion.id==models.EmotionTags.emotion_id))
         .join(models.Tag, on=(models.EmotionTags.tag_id==models.Tag.id))
         .where(models.Emotion.status==True)
         .group_by(models.Tag.id)
         )

    thoughts = (models.Thought
         .select(
           models.Tag.id.alias("tag_id")
         , fn.Count(models.Tag.id).alias("count")
         )
         .join(models.ThoughtTags, on=(models.Thought.id==models.ThoughtTags.thought_id))
         .join(models.Tag, on=(models.ThoughtTags.tag_id==models.Tag.id))
         .where(models.Thought.status==True)
         .group_by(models.Tag.id)
         )

    behaviors = (models.Behavior
          .select(
            models.Tag.id.alias("tag_id")
          , fn.Count(models.Tag.id).alias("count")
          )
          .join(models.BehaviorTags, on=(models.Behavior.id==models.BehaviorTags.behavior_id))
          .join(models.Tag, on=(models.BehaviorTags.tag_id==models.Tag.id))
          .where(models.Behavior.status==True)
          .group_by(models.Tag.id)
          )


# ETBs MAPPED TO TAGS (TAG IDS)
    emotions_df = pd.DataFrame(list(emotions.dicts()))
    thoughts_df = pd.DataFrame(list(thoughts.dicts()))
    behaviors_df = pd.DataFrame(list(behaviors.dicts()))

# COMBINE EBTs INTO ONE TABLE OF TAG COUNTS
    ebt_tag_count = pd.concat([emotions_df, thoughts_df, behaviors_df])
    ebt_totals = ebt_tag_count.groupby('tag_id').sum().reset_index()
    found_tag = ebt_totals.sort_values(by='count', ascending=False)
    found_tag = found_tag['tag_id'][0]

# MAP TAGS (TAG IDS) TO EXERCISE TAGS WHERE TAGS IN DFs
    exercise_tags = models.Exercise.select(models.Exercise.id.alias("exercise_id")
    , models.Exercise.name.alias("exercise_name")
    , models.ExerciseTags.tag_id.alias("exercise_tag_id")
    , models.Tag.tag.alias("tag")
    , models.Tag.id.alias("tag_id")
    ).join(models.ExerciseTags,
    on=models.Exercise.id==models.ExerciseTags.exercise_id).join(models.Tag, on=models.ExerciseTags.tag_id==models.Tag.id)

    exercise_tags_df = pd.DataFrame(list(exercise_tags.dicts()))

    answer = int(exercise_tags_df.loc[exercise_tags_df['tag_id']==found_tag]['exercise_id'].values[0])
    print(f"THE ANSWER IS {answer}")
    print(type(answer))

    models.Emotion.update(status=False)
    models.Thought.update(status=False)
    models.Behavior.update(status=False)


    new_suggestedexercise = models.SuggestedExercise.create(exercise = answer)
    suggestedexercise_dict = model_to_dict(new_suggestedexercise)
    return jsonify(
        data=suggestedexercise_dict,
        message=f'Successfully created suggestedexercise {answer}!',
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

#--------------------------------------------
# IMPORTS
#--------------------------------------------
import os
from playhouse.db_url import connect
from peewee import *
import datetime
from flask_login import UserMixin
from resources.seeds.exercises import exercises
from resources.seeds.tags import tags
from resources.seeds.exercise_tags import exercise_tags
from resources.seeds.emotions import emotions
from resources.seeds.emotion_tags import emotion_tags
from resources.seeds.thoughts import thoughts
from resources.seeds.thought_tags import thought_tags
from resources.seeds.behaviors import behaviors
from resources.seeds.behavior_tags import behavior_tags

#--------------------------------------------
# DATABASE ENVIRONMENT
#--------------------------------------------
# def select_database(environment):
#     if environment == 'development':
#         return SqliteDatabase('capstone.sqlite')
#     if environment == 'production':
#         return PostgresqlDatabase('capstone', user='postgres')
# DATABASE = select_database('development')
DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///capstone.sqlite')
#DATABASE_URL will exist on heroku
#--------------------------------------------
# CREATE MODELS
#--------------------------------------------
class User(UserMixin, Model):
    username=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField()
    class Meta:
        database = DATABASE
def add_user_seed():
    User(username='example',email='example@example.com',password='example').save()

class Exercise(Model):
    name = CharField()
    description=CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_exercise_seed():
    for exercise in exercises:
        Exercise(name=exercise[0], description=exercise[1]).save()

class SuggestedExercise(Model):
    # name = CharField()
    # description=CharField()
    exercise= ForeignKeyField(Exercise)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_exercise_seed():
    for exercise in exercises:
        Exercise(name=exercise[0], description=exercise[1]).save()

class UserExercise(Model):
    user= ForeignKeyField(User, backref="this_users_exercises")
    exercise = ForeignKeyField(Exercise)
    completed = BooleanField()
    completed_count = IntegerField()
    favorite = BooleanField()
    recommended = BooleanField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

class Tag(Model):
    tag = CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_tag_seed():
    for this_tag in tags:
        Tag(tag=this_tag).save()

class ExerciseTags(Model):
    exercise = ForeignKeyField(Exercise)
    tag = ForeignKeyField(Tag)
    # stretch: tag score
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_exercise_tags_seed():
    for t in exercise_tags:
        ExerciseTags(exercise=t[0], tag=t[1]).save()

class Emotion(Model):
    emotion = CharField()
    status = BooleanField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_emotion_seed():
    for i in emotions:
        Emotion(emotion=i, status=False).save()
class EmotionTags(Model):
    emotion = ForeignKeyField(Emotion)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_emotion_tags_seed():
    for i in emotion_tags:
        EmotionTags(emotion=i[0],tag=i[1]).save()
class Thought(Model):
    thought = CharField()
    status = BooleanField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_thought_seed():
    for i in thoughts:
        Thought(thought=i, status=False).save()
class ThoughtTags(Model):
    thought = ForeignKeyField(Thought)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_thought_tags():
    for t in thought_tags:
        ThoughtTags(thought=t[0], tag=t[1]).save()
class Behavior(Model):
    behavior = CharField()
    status = BooleanField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_behavior_seed():
    for i in behaviors:
        Behavior(behavior=i, status=False).save()
class BehaviorTags(Model):
    behavior = ForeignKeyField(Behavior)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_behavior_tags():
    for i in behavior_tags:
        BehaviorTags(behavior_id=i[0],tag_id=i[1]).save()



#--------------------------------------------
# ADD SEEDS
#--------------------------------------------
def add_seeds():
    # add_user_seed()
    add_exercise_seed()
    add_tag_seed()
    add_emotion_seed()
    add_emotion_tags_seed()
    add_exercise_tags_seed()
    add_thought_seed()
    add_thought_tags()
    add_behavior_seed()
    add_behavior_tags()

#--------------------------------------------
# INITIALIZE DATABASE AND TABLES
#--------------------------------------------
def initialize():
    DATABASE.connect()
    tables = [User, Exercise, SuggestedExercise, UserExercise, Tag, ExerciseTags, Emotion, Thought, Behavior, EmotionTags, ThoughtTags, BehaviorTags]
    for table in tables:
        DATABASE.drop_tables([table], safe=True)
        DATABASE.create_tables([table], safe=True)
    DATABASE.create_tables([User, Exercise, SuggestedExercise, UserExercise, Tag, ExerciseTags, Emotion, Thought, Behavior, EmotionTags, ThoughtTags, BehaviorTags], safe=True)
    print("Initialized database and tables...")
    add_seeds()
    DATABASE.close()

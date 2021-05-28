#--------------------------------------------
# IMPORTS
#--------------------------------------------
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
def select_database(environment):
    if environment == 'development':
        return SqliteDatabase('capstone.sqlite')
    if environment == 'production':
        return PostgresqlDatabase('capstone', user='postgres')
DATABASE = select_database('development')

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
    User(username='exampleUser',email='example@email.com',password='easyLogin').save()

class Exercise(Model):
    name = CharField()
    description=CharField()
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

# def add_list_seed(seed_model,seed_list,model_field):
#     for i in seed_list:
#         seed_model(model_field=i).save()

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
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_thought_seed():
    for i in thoughts:
        Thought(thought=i).save()
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
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_behavior_seed():
    for i in behaviors:
        Behavior(behavior=i).save()
class BehaviorTags(Model):
    behavior = ForeignKeyField(Behavior)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_behavior_tags():
    for i in behavior_tags:
        BehaviorTags(behavior_id=i[0],tag_id=i[1]).save()

class InputForm(Model):
    user= ForeignKeyField(User, backref="this_users_input_forms")
    Happy = BooleanField()
    Sad  = BooleanField()
    Angry  = BooleanField()
    Stressed  = BooleanField()
    Overwhelmed = BooleanField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
class InputFormTest(Model):
    user= ForeignKeyField(User, backref="this_users_input_forms")
    test='test'
    form_datetime=DateTimeField(default=datetime.datetime.now)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
class InputFormEmotions(Model):
    form = ForeignKeyField(InputForm)
    emotion = ForeignKeyField(Emotion)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
class InputFormThoughts(Model):
    form = ForeignKeyField(InputForm)
    emotion = ForeignKeyField(Thought)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
class InputFormBehaviors(Model):
    form = ForeignKeyField(InputForm)
    emotion = ForeignKeyField(Behavior)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

#--------------------------------------------
# ADD SEEDS
#--------------------------------------------
def add_seeds():
    add_user_seed()
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
    tables = [User, Exercise, UserExercise, Tag, ExerciseTags, Emotion, Thought, Behavior, EmotionTags, ThoughtTags, BehaviorTags, InputForm, InputFormEmotions, InputFormThoughts, InputFormBehaviors, InputFormTest]
    for table in tables:
        DATABASE.drop_tables([table], safe=True)
        DATABASE.create_tables([table], safe=True)
    print("Initialized database and tables...")
    add_seeds()
    DATABASE.close()

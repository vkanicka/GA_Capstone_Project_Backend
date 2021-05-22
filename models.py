
from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('capstone.sqlite') # DEV
# DATABASE = PostgresqlDatabase('capstone', user='postgres') # PROD

class User(UserMixin, Model):
    username=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField()
    class Meta:
        database = DATABASE

class Exercise(Model):
    name = CharField()
    description=CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

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

class ExerciseTags(Model):
    exercise = ForeignKeyField(Exercise)
    tag = ForeignKeyField(Tag)
    # stretch: tag score
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

class Emotion(Model):
    emotion = CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

class Thought(Model):
    thought = CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

class Behavior(Model):
    behavior = CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

class EmotionTags(Model):
    emotion = ForeignKeyField(Emotion)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

class ThoughtTags(Model):
    thought = ForeignKeyField(Thought)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

class BehaviorTags(Model):
    behavior = ForeignKeyField(Behavior)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

class InputForm(Model):
    user = ForeignKeyField(User)
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




def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Exercise, UserExercise, Tag, ExerciseTags, Emotion, Thought, Behavior, EmotionTags, ThoughtTags, BehaviorTags, InputForm, InputFormEmotions, InputFormThoughts, InputFormBehaviors], safe=True)
    print("Initialized database and tables...")
    DATABASE.close()

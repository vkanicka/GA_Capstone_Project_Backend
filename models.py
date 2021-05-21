
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

class ExerciseTags(Model):
    exercise = ForeignKeyField(Exercise)
    tag = ForeignKeyField(Tag)

class Feeling(Model):
    feeling = CharField()

class Thought(Model):
    thought = CharField()

class Behavior(Model):
    behavior = CharField()

class FeelingTags(Model):
    exercise = ForeignKeyField(Feeling)
    tag = ForeignKeyField(Tag)

class ThoughtTags(Model):
    exercise = ForeignKeyField(Thought)
    tag = ForeignKeyField(Tag)

class BehaviorTags(Model):
    exercise = ForeignKeyField(Behavior)
    tag = ForeignKeyField(Tag)




def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Exercise, UserExercise], safe=True)
    print("Initialized database and tables...")
    DATABASE.close()

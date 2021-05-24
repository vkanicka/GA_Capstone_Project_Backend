from peewee import *
import datetime
from flask_login import UserMixin

def select_database(environment):
    if environment == 'development':
        return SqliteDatabase('capstone.sqlite')
    if environment == 'production':
        return PostgresqlDatabase('capstone', user='postgres')
DATABASE = select_database('development')

class User(UserMixin, Model):
    username=CharField(unique=True)
    email=CharField(unique=True)
    password=CharField()
    class Meta:
        database = DATABASE
def add_user_seed():
    User(username='exampleUser',email='example@email.com',password='easyLogin').save()
    print('user seed added')

class Exercise(Model):
    name = CharField()
    description=CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_exercise_seed():
    exercises = [
    ("Diaphram Breathing", "Breathe in deeply..."),
 	("Time Management Exercise",	"Start by listing tasks..."),
 	("Self-Compassion Meditation",	"Close your eyes..."),
 	("Restorative Communicatio",	"Follow these steps..."),
 	("Explore Strengths",	"What are 10 things..."),
 	("Gratitude",	"Think of three specific..."),
    ]
    for exercise in exercises:
        Exercise(name=exercise[0], description=exercise[1]).save()
    print('exercise seed added')

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
    tags = [
    'Time Management',
    'Stress',
    'Self-Compassion',
    'Conflict',
    'Communication',
    'Depression',
    'Anxiety',
    'Social Anxiety',
    'Fear',
    'Anger',
    'Acceptance',
    'Self Esteem'
    ]
    for this_tag in tags:
        Tag(tag=this_tag).save()
    print('tag seed added')

class ExerciseTags(Model):
    exercise = ForeignKeyField(Exercise)
    tag = ForeignKeyField(Tag)
    # stretch: tag score
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_exercise_tags_seed():
    exercise_tags = [
    (1,2),
    (2,1),
    (2,2),
    (3,3),
    (4,4),
    (4,5)
    ]
    for t in exercise_tags:
        ExerciseTags(exercise=t[0], tag=t[1]).save()
    print('exercise tag seed added')

emotions = [
'Happy',
'Sad',
'Angry',
'Stressed',
'Overwhelmed',
'Annoyed'
]
class Emotion(Model):
    emotion = CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_emotion_seed():
    for this_emotion in emotions:
        Emotion(emotion=this_emotion).save()
    print('emotion seed added')
class EmotionTags(Model):
    emotion = ForeignKeyField(Emotion)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_emotion_tags_seed():
    emotion_tags = [
    (2,6),
    (3,4),
    (3,5),
    (3,10),
    (4,1),
    (4,2),
    (4,7),
    (5,1),
    (5,2),
    (5,6),
    (5,7),
    (6,4),
    (6,5),
    (6,10)
    ]

    for i in emotion_tags:
        EmotionTags(emotion=i[0],tag=i[1]).save()
    print('emotion tag seed added')

class Thought(Model):
    thought = CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_thought_seed():
    thoughts = [
    "I have no idea how to start",
 	"I will never finish this",
 	"Nothing matters",
 	"I want to give up",
 	"I wish I didn't feel this way",
 	"I should be more productive",
 	"My thoughts are racing",
 	"I am too (negative adjective)"
    ]
    for i in thoughts:
        Thought(thought=i).save()
    print('thought seed added')
class ThoughtTags(Model):
    thought = ForeignKeyField(Thought)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_thought_tags():
    thought_tags = [
    (1, 1),
    (2, 1),
    (2, 2),
    (3, 6),
    (4, 6),
    (5, 11),
    (6, 3),
    (7, 7),
    (8, 11),
    (8, 12)
    ]
    for t in thought_tags:
        ThoughtTags(thought=t[0], tag=t[1]).save()
    print('thought tag seed added')

class Behavior(Model):
    behavior = CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_behavior_seed():
    behaviors = [
    "Procrastinating",
 	"Overthinking",
 	"Avoiding",
 	"Withdrawing",
 	"Isolating"
    ]
    for i in behaviors:
        Behavior(behavior=i).save()
    print('behavior seed added')
class BehaviorTags(Model):
    behavior = ForeignKeyField(Behavior)
    tag = ForeignKeyField(Tag)
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
def add_behavior_tags():
    behavior_tags = [
    (1,1),
    (1,7),
    (2,1),
    (2,2),
    (2,7),
    (3,1),
    (3,4),
    (3,8),
    (3,9),
    (3,10),
    (4,4),
    (4,6),
    (4,8),
    (5,6),
    (5,8)
    ]
    for i in behavior_tags:
        BehaviorTags(behavior_id=i[0],tag_id=i[1]).save()
    print('behavior tags seed added')


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

def initialize():
    DATABASE.connect()
    tables = [User, Exercise, UserExercise, Tag, ExerciseTags, Emotion, Thought, Behavior, EmotionTags, ThoughtTags, BehaviorTags, InputForm, InputFormEmotions, InputFormThoughts, InputFormBehaviors, InputFormTest]
    for table in tables:
        DATABASE.drop_tables([table], safe=True)
        DATABASE.create_tables([table], safe=True)
    print("Initialized database and tables...")
    add_seeds()
    DATABASE.close()

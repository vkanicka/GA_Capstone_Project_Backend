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
        {'name': 'Time Management Exercise',
        'description': 'List tasks. Set due dates. Prioritize. Determine ONE next right thing. Do I know how to do this? Break down into specific manageable steps. Anything that feels overwhelming - break it down even more. Schedule the task. Set an alarm reminder and a timer.'
        },
        {'name': 'Self-Compassion Meditation',
        'description': '...tbd description...'
        },
        {'name': 'Diaphram Breathing',
        'description': 'Breathe in 5. Hold for 3. Breathe out 7.'
        },
        {'name': '54321 Grounding',
        'description': 'Count 5 things I see. Count 4 things I hear. Count 3 things I feel.'
        },
    ]
    for exercise in exercises:
        Exercise(name=exercise['name'], description=exercise['description']).save()
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
    (2,1),
    (2,2),
    (3,3),
    (1,2),
    (4,4),
    (4,5)
    ]
    for t in exercise_tags:
        print(t)
        ExerciseTags(exercise=t[0], tag=t[1]).save()
    print('exercise tag seed added')

class Emotion(Model):
    emotion = CharField()
    created_at: DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE

def add_emotion_seed():
    emotions = [
    'Happy',
    'Sad',
    'Angry',
    'Stressed',
    'Overwhelmed',
    'Annoyed'
    ]

    for this_emotion in emotions:
        Emotion(emotion=this_emotion).save()
    print('emotion seed added')

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

def add_emotion_tags_seed():
    emotion_tags = [
    {'emotion': 4, 'tag': 1},
    {'emotion': 5, 'tag': 1},
    {'emotion': 2, 'tag': 6}
    ]

    for i in emotion_tags:
        EmotionTags(emotion=i['emotion'],tag=i['tag']).save()
    print('emotion tag seed added')

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
    tables = [User, Exercise, UserExercise, Tag, ExerciseTags, Emotion, Thought, Behavior, EmotionTags, ThoughtTags, BehaviorTags, InputForm, InputFormEmotions, InputFormThoughts, InputFormBehaviors]
    for table in tables:
        DATABASE.drop_tables([table], safe=True)
        DATABASE.create_tables([table], safe=True)
    print("Initialized database and tables...")
    add_user_seed()
    add_exercise_seed()
    add_tag_seed()
    add_emotion_seed()
    add_emotion_tags_seed()
    add_exercise_tags_seed()
    DATABASE.close()

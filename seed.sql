TRUNCATE TABLE User
TRUNCATE TABLE Exercise
TRUNCATE TABLE UserExercise
TRUNCATE TABLE Tag
TRUNCATE TABLE ExerciseTags
TRUNCATE TABLE Emotion
TRUNCATE TABLE Thought
TRUNCATE TABLE Behavior
TRUNCATE TABLE EmotionTags
TRUNCATE TABLE ThoughtTags
TRUNCATE TABLE BehaviorTags
TRUNCATE TABLE InputForm
TRUNCATE TABLE InputFormEmotions
TRUNCATE TABLE InputFormThoughts
TRUNCATE TABLE InputFormBehaviors

ALTER SEQUENCE User  RESTART WITH 1;
ALTER SEQUENCE Exercise RESTART WITH 1;
ALTER SEQUENCE UserExercise RESTART WITH 1;
ALTER SEQUENCE Tag RESTART WITH 1;
ALTER SEQUENCE ExerciseTags RESTART WITH 1;
ALTER SEQUENCE Emotion RESTART WITH 1;
ALTER SEQUENCE Thought RESTART WITH 1;
ALTER SEQUENCE Behavior RESTART WITH 1;
ALTER SEQUENCE EmotionTags RESTART WITH 1;
ALTER SEQUENCE ThoughtTags RESTART WITH 1;
ALTER SEQUENCE BehaviorTags RESTART WITH 1;
ALTER SEQUENCE InputForm RESTART WITH 1;
ALTER SEQUENCE InputFormEmotions RESTART WITH 1;
ALTER SEQUENCE InputFormThoughts RESTART WITH 1;
ALTER SEQUENCE InputFormBehaviors RESTART WITH 1;

INSERT INTO User (username, email, password) VALUES ('Example Name',         'example@email.com', 'examplePassword');

INSERT INTO Exercise (name, description) VALUES ('Time Management Exercise', 'List tasks. Set due dates. Prioritize. Determine ONE next right thing. Do I know how to do this? Break down into specific manageable steps. Anything that feels overwhelming - break it down even more. Schedule the task. Set an alarm reminder and a timer.');

INSERT INTO Exercise (name, description) VALUES ('Self-Compassion Meditation', '...tbd description...');

INSERT INTO Exercise (name, description) VALUES ('Diaphram Breathing', 'Breathe in 5. Hold for 3. Breathe out 7.');

INSERT INTO Exercise (name, description) VALUES ('54321 Grounding', 'Count 5 things I see. Count 4 things I hear. Count 3 things I feel.');

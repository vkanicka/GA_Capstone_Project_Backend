# GA_Capstone_Project_Backend

#### Link to Hosted Working App
 - [ ] tbd 

#### Description 
An app that matches a user's current thoughts, feelings and behaviors with mental health exercises specific to their needs.

#### Technologies Used
Python, Flask, SQL, React 

#### Installation Steps
 - [ ] tbd

## Who
Users of this app understand the importance of mental health, but want a more interactive, hands-on way to learn and practice mental health strengthening techniques than traditional therapy, workbooks, or audio/video meditation. May scale for therapists and counselors.

## User Stories (MVP)
 - [ ] Users can create an account and login
 - [ ] Users can communicate how they’re doing to the app via a selection of inputs that may include emojis, sliders and clickable buttons for emotions, thoughts and behaviors
 - [ ] User will receive mirroring response from app (Ex. “It sounds like you may be feeling ______, is that right?)
 - [ ] Users can receive suggestion(s) on what exercises to complete within the app based on their daily input

## Stretch Features
 - [ ] App may ask user follow up questions to better estimate most helpful path for user
 - [ ] User can create customizable avatar
 - [ ] Exercises will feature helper characters (ex. Psychic, scientist, etc.)
 - [ ] Exercises will have tags to help user and app search for appropriate exercises
 - [ ] User will receive summary of session (optional: via email?)
 - [ ] Exercises will have a timer with recommended amount of time (Ex. 5minutes, 3-10minutes)
 - [ ] App will track and visualize user’s progress in building various skills
 - [ ] User has a dashboard where certain features are posted (ex. Focus: next right thing, to do list prioritized)
 - [ ] If user is feeling great and app cannot determine a specific time sensitive focus area, app will let user decide which exercise to complete

## Wireframes
 - [ ] Option 1: Just input, feedback and suggested exercise
 - [ ] Option 2: Dashboard with widgets and progress tracking
 - [ ] Option 3: Avatar personalization

## Data Models
 - [ ] Exercise
 - [ ] User

## Entity Relationship Diagrams
Exercises
Key | Name | Description
------------ | -------------  | -------------
1 | Diaphram Breathing | Breathe in deeply...
2 | Time Management Exercise | Start by listing tasks...
3 | Self-Compassion Meditation | Close your eyes...
4 | Restorative Communication | Follow these steps...
5 | Explore Strengths | What are 10 things...
6 | Gratitude | Think of three specific...

Tags
Key | Tag
------------ | -------------
1 | Time Management
2 | Stress
3 | Self-Compassion
4 | Conflict
5 | Communication
6 | Depression
7 | Anxiety
8 | Social Anxiety
9 | Fear
10 | Anger
11 | Acceptance
12 | Self Esteem

Feelings
Key | Feeling
------------ | -------------
1 | Happy
2 | Sad
3 | Angry
4 | Stressed 
5 | Overwhelmed
6 | Annoyed

Exercise Tags
Key | Exercise ID | Tag ID
------------ | ------------- | -------------
1 | 2 | 1
2 | 2 | 2
3 | 3 | 3
4 | 1 | 2
5 | 4 | 4
6 | 4 | 5

Thoughts
Key | Thought
------------ | -------------
1 | I have no idea how to start
2 | I will never finish this
3 | Nothing matters
4 | I want to give up 
5 | I wish I didn't feel this way
6 | I should be more productive
7 | My thoughts are racing
8 | I am too _(negative adjective)_

Behaviors
Key | Behavior
------------ | -------------
1 | Procrastinating
2 | Overthinking
3 | Avoiding
4 | Withdrawing
5 | Isolating

Feelings Tags
Key | Feeling ID | Tag ID
------------ | ------------- | -------------
1 | 2 | 1
2 | 2 | 1
3 | 3 | 3
4 | 1 | 2
5 | 4 | 4
5 | 4 | 4

Thought Tags
Key | Thought ID | Tag ID
------------ | ------------- | -------------
1 | 1 | 1
2 | 2 | 2
3 | 3 | 6
4 | 4 | 6
5 | 5 | 11
6 | 6 | 3
7 | 7 | 7
8 | 8 | 11
8 | 8 | 12

Behavior Tags
Key | Behavior ID | Tag ID
------------ | ------------- | -------------
1 | 2 | 1
2 | 2 | 7
3 | 3 | 1
3 | 3 | 4
3 | 3 | 8
3 | 3 | 9
3 | 3 | 10
4 | 4 | 4
4 | 4 | 6
4 | 4 | 8
5 | 5 | 6
5 | 5 | 8

Exercise Length
Key | Count | Type
------------ | ------------- | -------------
1 | 1 | minute(s)
2 | 3 | minute(s)
3 | 5 | minute(s)
4 | 10 | minute(s)
5 | 1 | time(s)
6 | 3 | time(s)
7 | 5 | time(s)
8 | 10 | time(s)



## Unsolved Problems and Future Features
 - [ ] tbd

#--------------------------------------------
# IMPORTS
#--------------------------------------------
from flask import Flask, jsonify, after_this_request #, g
from resources.exercises import exercises
from resources.suggestedexercises import suggestedexercises
from resources.users import users
from resources.userexercises import userexercises
from resources.emotion import emotion
from resources.thought import thought
from resources.behavior import behavior
from resources.reset_tables import reset
import models
from flask_cors import CORS
from flask_login import LoginManager
import os
from dotenv import load_dotenv
from resources.filelist import string_model_list

#--------------------------------------------
# CONSTANT VARIABLES / ENV
#--------------------------------------------
load_dotenv() # takes the environment variables from .env
DEBUG=True # print error msgs since we're in development
PORT=8000

#--------------------------------------------
# CREATE app
#--------------------------------------------
app = Flask(__name__)

#--------------------------------------------
# LOGIN MANAGER CONFIGURATION
#--------------------------------------------
app.secret_key = os.environ.get("FLASK_APP_SECRET")
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return models.User.get(models.User.id == user_id)

#--------------------------------------------
# CORS
#--------------------------------------------
# CORS(exercises, origins=['http://localhost:3000'], # supports_credentials=True
# )
# CORS(suggestedexercises, origins=['http://localhost:3000'], # supports_credentials=True
# )
# CORS(users, origins=['http://localhost:3000']
# #, supports_credentials=True
# )
# CORS(userexercises, origins=['http://localhost:3000'], # supports_credentials=True
# )
# CORS(emotion, origins=['http://localhost:3000'], # supports_credentials=True
# )
# CORS(thought, origins=['http://localhost:3000'], #supports_credentials=True
# )
# CORS(behavior, origins=['http://localhost:3000'], #supports_credentials=True
# )
# CORS(reset, origins=['http://localhost:3000'], supports_credentials=True)

model_list=[exercises, suggestedexercises, users, userexercises, emotion, thought, behavior, reset]

for model in model_list:
    CORS(model, origins=['http://localhost:3000', 'https://mental-health-trainer.herokuapp.com'])

# for model in model_list:
#     CORS(model, origins=['https://mental-health-trainer.herokuapp.com'], supports_credentials=True)

#--------------------------------------------
# REGISTER BLUEPRINTS
#--------------------------------------------
app.register_blueprint(exercises, url_prefix='/exercises')
app.register_blueprint(suggestedexercises, url_prefix='/suggestedexercises')
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(userexercises, url_prefix='/userexercises')
app.register_blueprint(emotion, url_prefix='/emotion')
app.register_blueprint(thought, url_prefix='/thought')
app.register_blueprint(behavior, url_prefix='/behavior')
app.register_blueprint(reset, url_prefix='/reset')

#--------------------------------------------
# DEFERRED CALLBACKS
#--------------------------------------------
@app.before_request
def before_request():
    """Connect to the db before each request"""
    print("before_request")
    models.DATABASE.connect()

@app.after_request
def after_request(response):
    """Close the db connetion after each request"""
    print("after_request")
    models.DATABASE.close()
    return response

#--------------------------------------------
# INTIALIZE DATABASE TABLES
#--------------------------------------------
# DEVELOPMENT
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

# PRODUCTION:
if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()

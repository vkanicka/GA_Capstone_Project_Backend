#--------------------------------------------
# IMPORTS
#--------------------------------------------
from flask import Flask, g, jsonify
from resources.exercises import exercises
from resources.users import users
from resources.userexercises import userexercises
from resources.inputforms import inputforms
from resources.inputformstest import inputformstest
import models
from flask_cors import CORS
from flask_login import LoginManager
import os
from dotenv import load_dotenv

model_list = [users,exercises,userexercises,inputforms, inputformstest
# ,tag,exercisetags,emotion,thought,behavior,emotiontags,thoughttags,behaviortags,inputform,inputformemotions,inputformthoughts,inputformbehaviors
]

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
# DATABASE COMMUNICATION
#--------------------------------------------
@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

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
for model in model_list:
    CORS(model, origins=['http://localhost:3000'], supports_credentials=True)
#--------------------------------------------
# REGISTER BLUEPRINTS
#--------------------------------------------
    app.register_blueprint(model, url_prefix=f'/api/v1/{str(__name__)}')

#--------------------------------------------
# CREATE TABLES AND RUN APP
#--------------------------------------------
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

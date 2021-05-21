#--------------------------------------------
# IMPORTS
#--------------------------------------------
from flask import Flask, g, jsonify
from resources.exercises import exercises
from resources.users import users
from resources.userexercises import userexercises
import models
from flask_cors import CORS
from flask_login import LoginManager
import os
from dotenv import load_dotenv

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
CORS(exercises, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(userexercises, origins=['http://localhost:3000'], supports_credentials=True)

#--------------------------------------------
# REGISTER BLUEPRINTS
#--------------------------------------------
app.register_blueprint(exercises, url_prefix='/api/v1/exercises')
app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(userexercises, url_prefix='/api/v1/userexercises')


#--------------------------------------------
# CREATE TABLES AND RUN APP
#--------------------------------------------
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

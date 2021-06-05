#--------------------------------------------
# IMPORTS
#--------------------------------------------
import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user#, login_required

#--------------------------------------------
# CREATE BLUEPRINT
#--------------------------------------------
reset = Blueprint('reset', 'reset')

    # DEVELOPMENT:
    # import sqlite3
    # con = sqlite3.connect('capstone.sqlite')
    # cur = con.cursor()
    # cur.execute('''
    # UPDATE '''+type+'''
    # SET status=False
    # ;
    # ''')
    # con.commit()
    # con.close()


#--------------------------------------------
# RESET EMOTIONS
#--------------------------------------------

@reset.route('/', methods=["PUT"])
def reset_tables():
    models.Emotion.update(status=False)
    models.Thought.update(status=False)
    models.Behavior.update(status=False)
    return('reset tables')

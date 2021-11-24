from flask import Flask
from app.models import User, Post
# from congif import Config

@app.shell_context_processor
def make_shell_context():
    return{'db': db, 'User': User, 'Post': Post}

# app = Flask(_name_)
# app.config.from_object(Config)

# from app import routes

# (venv) $ export FLASK-APP = microblog.py

# (venv) $ flask run

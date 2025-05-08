"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger

# Set up logging
logging.basicConfig(level=logging.WARNING)  # Set the logging level to WARNING
streamHandler = logging.StreamHandler()  # Create a stream handler
streamHandler.setLevel(logging.WARNING)  # Set the handler level to WARNING
app.logger.addHandler(streamHandler)  # Add the handler to the app's logger

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views

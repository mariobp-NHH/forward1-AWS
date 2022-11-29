from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

from webse.forward_home.routes import forward_home

application.register_blueprint(forward_home)

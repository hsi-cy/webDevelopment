from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# double underscore name is a name of the module. if we run the script with python directly then double underscore name can be equal to double underscore main
app = Flask(__name__)
# Create a secure cookie
app.config['SECRET_KEY'] = 'e3320a22f374154e50bb8750f68275c3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# we can use database as classes
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes

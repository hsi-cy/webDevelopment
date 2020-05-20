from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
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
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'antoniomaroco37@gmail.com'
app.config['MAIL_PASSWORD'] = ''
mail = Mail(app)

from flaskblog import routes

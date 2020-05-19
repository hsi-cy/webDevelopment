from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# double underscore name is a name of the module. if we run the script with python directly then double underscore name can be equal to double underscore main
app = Flask(__name__)
# Create a secure cookie
app.config['SECRET_KEY'] = 'e3320a22f374154e50bb8750f68275c3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# we can use database as classes
db = SQLAlchemy(app)

from flaskblog import routes
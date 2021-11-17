import os
import sys
sys.path.append(
    "/Users/raysal/Documents/Python Projects/Rest APIs/Flask/People_Part2/.venv/lib/python3.9/site-packages")
import connexion
# allows you to interact with the database without having to write SQL
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# creates the variable basedir pointing to the directory the program is running in
basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)

# Create connexion application instance
# use basedir variable to create Connexion app instance and give it
# the path to the swagger.yml
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask instance
app = connex_app.app

# Configure the SQLAlchemy part of the instance
# This causes  SQLALchemy to echo SQL statements it executes to the console
app.config['SQLALCHEMY_ECHO'] = True
# This tells SQLALchemy to use sqlite as the database and a file named people.db
# in the current directory as the database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'people.db')
# turns off the SQLAlchemy event system
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
# initialized after the SQLAlchemy so that it can introspect SQLAlchemy components
# attached to the app
ma = Marshmallow(app)

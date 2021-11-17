import os
import sys
sys.path.append(
    "/Users/raysal/Documents/Python Projects/Rest APIs/Flask/Greatest NBA Players/.venv/lib/python3.9/site-packages")
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'players.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

import sys
sys.path.append(
    "/Users/raysal/Documents/Python Projects/Rest APIs/Flask/Greatest NBA Players/.venv/lib/python3.9/site-packages")

from flask import make_response, abort
from config import db
from models import Player, PlayerSchema


def read_all():
    """
    This function responds to a request for /api/players with the
    complete list of players.
    :return: json string list of players
    """
    players = Player.query.order_by(Player.lname).all()
    # if there will be no parametere many=True, it will return an empty ({})
    # dictionary
    players_schema = PlayerSchema(many=True)
    data = players_schema.dump(players)
    return data

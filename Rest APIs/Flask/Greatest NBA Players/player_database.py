import os
from config import db
from models import Player

PLAYERS = [
    {'jersey_no': 23, 'fname': 'Michael', 'lname': 'Jaworski'},
    {'jersey_no': 8, 'fname': 'Kobe', 'lname': 'Saya'},
    {'jersey_no': 6, 'fname': 'Melo', 'lname': 'Gao'}]

if os.path.exists('players.db'):
    os.remove('players.db')

db.create_all()

for player in PLAYERS:
    p = Player(jersey_no=player['jersey_no'],
               fname=player['fname'], lname=player['lname'])
    db.session.add(p)
db.session.commit()

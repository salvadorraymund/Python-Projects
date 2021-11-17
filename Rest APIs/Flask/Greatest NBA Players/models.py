from datetime import datetime
from config import db, ma


class Player(db.Model):
    __tablename__ = 'players'
    player_id = db.Column(db.Integer, primary_key=True)
    jersey_no = db.Column(db.Integer)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        sqla_session = db.session
        load_instance = True

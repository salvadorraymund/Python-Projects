from datetime import datetime
from config import db, ma


class Person(db.Model):
    # name of the database. this is the people.db that
    # app.config[SQLALCHEMY_DATABASE_URI] looks for
    __tablename__ = 'people'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    notes = db.relationship(
        'Note',
        backref='person',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Note.timestamp)')


# Schema represents what's in the object
# Serializing means converting Python objects to simpler data structures such as JSON
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        sqlasession = db.session
        load_instance = True

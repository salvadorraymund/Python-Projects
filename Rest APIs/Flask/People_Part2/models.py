from datetime import datetime
from config import db, ma
from marshmallow import fields


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
        # 'Note' is the name of the class that initializes the db for notes
        'Note',
        # backref='person',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Note.timestamp)')


class Note(db.Model):
    __tablename__ = 'note'
    note_id = db.Column(db.Integer, primary_key=True)
    # encountered a NoForeignKey Error when I followed the article and used
    # people.person_id instead. db.ForeignKey refers to the __tablename__
    person_id = db.Column(db.Integer, db.ForeignKey('people.person_id'))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# Schema represents what's in the object
# Serializing means converting Python objects to simpler data structures such as JSON
class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        sqlasession = db.session
        load_instance = True
    # the notes attribute has a nested relationship with the PersonNoteSchema
    # it will default to an empty list if nothing is present in SQLAlchemy note relationship
    # many=True indicates that this is a one-to-many relationship
    notes = fields.Nested("PersonNoteSchema", default=[], many=True)

# defines what a Note object looks like as Marshmallow serializes the notes list


class PersonNoteSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recurssion issue
    """
    note_id = fields.Int()
    person_id = fields.Int()
    content = fields.Str()
    timestamp = fields.Str()

# defines what a Note object looks like in terms of Marshmallow


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        sqlasession = db.session
        load_instance = True
    # since it doesn't have many=True parameter, it means it's connected
    # only to a single person
    person = fields.Nested("NotePersonSchema", default=None)

# defines what is nested in the NoteSchema.person attribute


class NotePersonSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recurssion issue
    """
    person_id = fields.Int()
    lname = fields.Str()
    fname = fields.Str()
    timestamp = fields.Str()

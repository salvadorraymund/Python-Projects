
import sys
sys.path.append(
    "/Users/raysal/Documents/Python Projects/Rest APIs/Flask/People_Part2/.venv/lib/python3.9/site-packages")
from flask import make_response, abort
from config import db
from models import Person, Note, NoteSchema


def read_all():
    """
    This function responds to a request for /api/people/notes
    with the complete list of notes, sorted by note timestamp
    :return: json list of all notes for all people
    """
    # Query database for all notes
    notes = Note.query.order_by(db.desc(Note.timestamp)).all()

    # Serialize the list of notes from our data
    # encountered a Value error if I followed the tutorial where it included
    # "exclude=[person.note]"
    note_schema = NoteSchema(many=True)
    data = note_schema.dump(notes)
    return data


def read_one(person_id, note_id):
    """
    This function responds to a request for
    /api/people/{person_id}/notes/{note_id}
    with one matching note for the associated person

    :param person_id: Id of the person the note is related to
    :param note_id: Id of the note
    :return: json string of the note contents
    """
    # Query database for the note
    note = (
        Note.query.join(Person, Person.person_id == Note.person_id)
        .filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none())
    if note is not None:
        note_schema = NoteSchema()
        data = note_schema.dump(note)
        return data
    else:
        abort(
            404, f"Note not found for id: {note_id}")


def create(person_id, note):
    """
    This function creates a new note related to the passed person_id

    :param person_id: Id of the person the note is related to
    :param note: Id of the note to be created
    :return: 201 on success
    """
    # get the parent person
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is None:
        abort(404, f'Person not found for ID:{person_id}')

    # Create a NoteSchema instance
    schema = NoteSchema()
    new_note = schema.load(note, session=db.session).data

    # Add the note to the person and db
    person.notes.append(new_note)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_note).data
    return data, 201


def update(person_id, note_id, note):
    update_note = (Note.query.filter(Person.person_id == person_id).filter(
        Note.note_id == note_id).one_or_none())
    # Did we find an existing note?
    if update_note is not None:
        # turn the passed in note to a db object
        schema = NoteSchema()

        # Set the ids to the note we want to update
        # the method load deserializes data structure to an object
        update = schema.load(note, session=db.session)
        update.person_id = update_note.person_id
        update.note_id = update_note.note_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated note in the response
        data = schema.dump(update_note)
        return data, 200
    else:
        abort(404, f'Note not found for ID: {person_id}')


def delete(person_id, note_id):
    note = (
        Note.query.filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
            .one_or_none())
    if note is not None:
        db.session.delete(note)
        db.session.commit()
        return make_response(
            "Note {note_id} has now been deleted".format(note_id=note_id), 200)

    else:
        abort(404, f'No note found for Id: {note_id}')

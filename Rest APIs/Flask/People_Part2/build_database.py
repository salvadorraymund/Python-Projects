import os
from config import db
from models import Person
from note_model import Note
# Data to initialize database with

PEOPLE = [
    {'fname': 'Doug',
     'lname': 'Farrell',
     'notes': [('Cool, a mini-bloggin application!', '2019-01-06 22:17:54'),
               ('This could be useful', '2019-01-08 22:17:54'),
               ('Well, sort of useful', '2019-01-10 22:17:54'),
               ]},
    {'fname': 'Kent',
     'lname': 'Brockman',
     'notes': [
         ('Im going to make really profound observations', '2019-01-07 22:17:54'),
         ('Maybe theyll be more obvious than I thought', '2019-02-06 22:17:54'),
     ]},
    {'fname': 'Bunny',
     'lname': 'Easter',
     'notes': [
         ('Has anyone seen my easter eggs', '2019-01-07 22:17:54'),
         ('Im really late delivering these!', '2019-04-06 22:17:54'),
     ]}
]

# Delete database file if it exists already
if os.path.exists('people.db'):
    os.remove('people.db')

# Create database
db.create_all()


# Iterate over the PEOPLE structure and populate the databse
for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'])
    for note in person.get('notes'):
        content, timestamp = note
        p.notes.append(
            Note(content=content,
                 timestamp=datetime.strptime(timestamp, % Y - %m - %d % H: % M: % S),
                 ))
    db.session.add(p)
db.session.commit()

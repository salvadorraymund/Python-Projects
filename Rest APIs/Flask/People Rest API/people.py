"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""
import sys
sys.path.append(
    "/Users/raysal/Documents/Python Projects/Rest APIs/Flask/People Rest API/.venv/lib/python3.9/site-packages")
# System modules
from datetime import datetime

from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    # create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def read_one(lname):
    """
    This function responds to a request for api/people/{lname}
    with one matching person from people

    :param lname: last name of the person to find
    :return: person matching lname
    """
    # Does the person exist in people?
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname))


def create(person):
    """
    This function creates a new person in the structure
    based on the passed data
    :param person: person to create in people structure
    :return: 201 on Success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    # Does this person exist already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lname} succesfully created".format(lname=lname), 201)
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname))


def update(lname, person):
    """
    This function updates an existing person in the structure
    :param lname: last name of the person to update
    :param person: person to update
    :return: updated person structure
    """
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get('fname')
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404, "Person with lastname {lname} not found".format(lname=lname))


def delete(lname):
    """
    This function deletes a person from the structure
    :param lname: lname of the person to delete
    :return: 200 on successful, 404 if not found
    """
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{lname} succesfully deleted".format(lname=lname), 200)
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname))

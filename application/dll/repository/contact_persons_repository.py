from application.dll.db import session
from application.dll.models import ContactPersons


def create_contact_person(contact_person: dict):
    contact_person = ContactPersons(**contact_person)
    session.add(contact_person)
    session.commit()


def remove_contact_person(_id: int):
    contact_person = session.query(ContactPersons).filter(ContactPersons.contact_id == _id).first()
    session.delete(contact_person)
    session.commit()


def update_contact_person(_id: int, column: str, update: str):
    session.query(ContactPersons).filter(ContactPersons.contact_id == _id).update({column: update})
    session.commit()

from application.dll.db import session
from application.dll.models import ContactPersons
import re


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


def order_by_contact_person(column: str):
    return [{
                'contact_id': contact_person.contact_id,
                'first_name': contact_person.first_name,
                'last_name': contact_person.last_name,
                'email': contact_person.email,
                'phone': contact_person.phone
            } for contact_person in session.query(ContactPersons).order_by(column)]


def search_for_contact_person(column: str, search_for: str):
    contact_person = session.query(ContactPersons).all()
    return [{
                'contact_id': contact_person.contact_id,
                'first_name': contact_person.first_name,
                'last_name': contact_person.last_name,
                'email': contact_person.email,
                'phone': contact_person.phone
            } for customer in contact_person if re.search(search_for, getattr(customer, column))]

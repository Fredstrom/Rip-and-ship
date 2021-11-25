from application.dll.db import session
from application.dll.models import ContactPersons


def create_contact_person(contact_person):
    contact_person = ContactPersons(**contact_person)
    session.add(contact_person)
    session.commit()

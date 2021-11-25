from application.dll.repository import contact_persons_repository


def create_contact_person(contact_person):
    contact_persons_repository.create_contact_person(contact_person)

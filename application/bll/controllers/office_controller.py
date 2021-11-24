from application.dll.repository import offices_repository


def create_office(office):
    offices_repository.create_office(office)

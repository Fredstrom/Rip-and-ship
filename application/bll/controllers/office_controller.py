from application.dll.repository import offices_repository


def create_office(office):
    offices_repository.create_office(office)

def remove_office(_id):
    offices_repository.remove_office(_id)


def update_manufacturer(_id, column, update):
    offices_repository.update_office(_id, column, update)

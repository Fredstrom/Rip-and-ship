from application.dll.repository import manufacturer_repository


def create_manufacturer(manufacturer):
    manufacturer_repository.create_manufacturer(manufacturer)


def remove_manufacturer(_id):
    manufacturer_repository.remove_manufacturer(_id)


def update_manufacturer(_id, column, update):
    manufacturer_repository.update_manufacturer(_id, column, update)

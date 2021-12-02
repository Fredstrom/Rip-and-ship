from application.dll.repository import manufacturer_repository


def create_manufacturer(manufacturer):
    manufacturer_repository.create_manufacturer(manufacturer)


def remove_manufacturer(_id):
    manufacturer_repository.remove_manufacturer(_id)


def update_manufacturer(_id, column, update):
    manufacturer_repository.update_manufacturer(_id, column, update)


def get_manufacturer_by_id(_id):
    return manufacturer_repository.get_manufacturer_by_id(_id)


def order_by_manufacturer(column):
    manufacturer_repository.order_by_manufacturer(column)


def search_for_manufacturer(column, search_for):
    manufacturer_repository.search_for_manufacturer(column, search_for)

from application.dll.repository import office_repository


def create_office(office):
    office_repository.create_office(office)


def remove_office(_id):
    office_repository.remove_office(_id)


def update_office(_id, column, update):
    office_repository.update_office(_id, column, update)


def get_office_by_id(_id):
    office_repository.get_office_by_id(_id)


def order_by_office(column):
    return office_repository.order_by_office(column)


def search_for_office(column, search_for):
    return office_repository.search_for_office(column, search_for)

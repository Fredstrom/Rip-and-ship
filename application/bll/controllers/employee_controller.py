from application.dll.repository import employee_repository


def create_employee(employee):
    employee_repository.create_employee(employee)


def remove_employee(_id):
    employee_repository.remove_employee(_id)


def update_employee(_id, column, update):
    employee_repository.update_employee(_id, column, update)


def get_employee_by_id(_id):
    return employee_repository.get_employee_by_id(_id)


def order_by_employee(column):
    return employee_repository.order_by_employee(column)


def search_for_employee(column, search_for):
    return employee_repository.search_for_employee(column, search_for)

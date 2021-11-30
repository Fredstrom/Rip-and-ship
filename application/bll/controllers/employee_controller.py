from application.dll.repository import employee_repository


def create_employee(employee):
    employee_repository.create_employee(employee)


def remove_employee(_id):
    employee_repository.remove_employee(_id)


def update_employee(_id, column, update):
    employee_repository.update_employee(_id, column, update)

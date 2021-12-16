from application.dll.mongo.repository import employee_repository


def create_employee(employee: dict):
    employee_repository.create_employee(employee)


def remove_employee(**kwargs):
    employee_repository.remove_employee(**kwargs)


def update_employee(column: str, update, _id):
    employee_repository.update_employee(column, update, _id)


def get_employee_by_id(**kwargs) -> list:
    return employee_repository.get_employee_by_id(**kwargs)


def order_by_employee(column: str) -> list:
    return employee_repository.order_by_employee(column)


def search_for_employee(column: str, search_for: str) -> list:
    return employee_repository.search_for_employee(column, search_for)


def get_all_employees() -> list:
    return employee_repository.get_all_employees()

from application.dll.repository import customer_repository


def create_customer(customer: dict):
    customer_repository.create_customer(customer)


def remove_customer(_id: int):
    customer_repository.remove_customer(_id)


def update_customer(_id: int, column: str, update: str):
    customer_repository.update_customer(_id, column, update)

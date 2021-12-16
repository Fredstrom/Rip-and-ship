from application.dll.mongo.repository import customer_repository


def create_customer(customer: dict):
    customer_repository.create_customer(customer)


def remove_customer(**kwargs):
    customer_repository.remove_customer(**kwargs)


def update_customer(column: str, update, _id):
    customer_repository.update_customer(column, update, _id)


def get_customer_by_id(**kwargs) -> list:
    return customer_repository.get_customer_by_id(**kwargs)


def order_by_customer(column: str) -> list:
    return customer_repository.order_by_customer(column)


def search_for_customer(column: str, search_for: str) -> list:
    return customer_repository.search_for_customer(column, search_for)


def get_all_customer() -> list:
    return customer_repository.get_all_customers()


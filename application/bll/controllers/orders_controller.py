from application.dll.repository import orders_repository


def create_orders(orders):
    orders_repository.create_orders(orders)


def remove_order(_id: int):
    orders_repository.create_orders(_id)


def update_order(_id: int, column: str, update: str):
    orders_repository.update_order(_id, column, update)


def get_order_by_id(_id):
    orders_repository.get_order_by_id(_id)


def order_by_order(column):
    return orders_repository.order_by_order(column)


def search_for_order(column, search_for):
    return orders_repository.search_for_order(column, search_for)


def get_all_orders():
    return orders_repository.get_all_orders()

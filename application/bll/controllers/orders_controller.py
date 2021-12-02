from application.dll.repository import orders_repository


def create_orders(orders):
    orders_repository.create_orders(orders)

def remove_order(_id: int):
    orders_repository.create_orders(_id)

def update_order(_id: int, column: str, update: str):
    orders_repository.update_order(_id, column, update)

def get_order_by_id(_id):
    orders_repository.get_order_by_id(_id)

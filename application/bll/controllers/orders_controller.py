from application.dll.repository import orders_repository


def create_orders(orders):
    orders_repository.create_orders(orders)


from application.dll.repository import orders_repository


def create_orders(orders):
    orders_repository.create_orders(orders)


def order_by_order(column):
    return orders_repository.order_by_order(column)


def search_for_order(column, search_for):
    orders_repository.search_for_order(column, search_for)

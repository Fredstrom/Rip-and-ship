from application.dll.repository import orders_from_manufacturers_repository


def create_orders_from_manufacturers(order_from_manufacturer):
    orders_from_manufacturers_repository.create_orders_from_manufacturers(order_from_manufacturer)
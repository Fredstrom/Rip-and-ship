from application.dll.repository import orders_from_suppliers_repository


def create_orders_from_suppliers(order_from_supplier):
    orders_from_suppliers_repository.create_orders_from_suppliers(order_from_supplier)


from application.dll.db import session
from application.dll.models import OrdersFromSuppliers


def create_orders_from_suppliers(order_from_supplier):
    order_from_supplier = OrdersFromSuppliers(**order_from_supplier)
    session.add(order_from_supplier)
    session.commit()

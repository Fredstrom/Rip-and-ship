from application.dll.db import session
from application.dll.models import OrdersFromManufacturers


def create_orders_from_manufacturers(order_from_manufacturer):
    order_from_manufacturer = OrdersFromManufacturers(**order_from_manufacturer)
    session.add(order_from_manufacturer)
    session.commit()

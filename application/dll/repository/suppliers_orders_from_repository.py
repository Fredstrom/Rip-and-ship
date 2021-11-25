from application.dll.db import session
from application.dll.models import SuppliersOrdersFrom


def create_suppliers_orders_from(supplier_order_from):
    supplier_order_from = SuppliersOrdersFrom(**supplier_order_from)
    session.add(supplier_order_from)
    session.commit()

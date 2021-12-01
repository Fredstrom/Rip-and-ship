import re

from application.dll.db import session
from application.dll.models import Orders


def create_orders(orders):
    orders = Orders(**orders)
    session.add(orders)
    session.commit()


def order_by_order(column):
    return [{
                'order_id': order.order_id,
                'order_date': order.order_date,
                'delivery_date': order.delivery_date,
                'customer_id': order.customer_id,
                'employee_id': order.employee_id
            } for order in session.query(Orders).order_by(column)]


def search_for_order(column, search_for):
    orders = session.query(Orders).all()
    return [{
                'order_id': order.order_id,
                'order_date': order.order_date,
                'delivery_date': order.delivery_date,
                'customer_id': order.customer_id,
                'employee_id': order.employee_id
            } for order in orders if re.search(search_for, getattr(order, column))]
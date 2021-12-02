from application.dll.db import session
from application.dll.models import Orders
import re


def create_orders(orders):
    orders = Orders(**orders)
    session.add(orders)
    session.commit()


def remove_order(_id: int):
    contact_person = session.query(Orders).filter(Orders.order_id == _id).first()
    session.delete(contact_person)
    session.commit()


def update_order(_id: int, column: str, update: str):
    session.query(Orders).filter(Orders.order_id == _id).update({column: update})
    session.commit()


def get_order_by_id(_id):
    order = session.query(Orders).filter(Orders.order_id == _id).first()
    return {i.name: getattr(order, i.name) for i in order.table.columns}


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


def get_all_orders():
    orders = session.query(Orders).all()
    dict_list = []
    for order in orders:
        dict_list.append({i.name: getattr(order, i.name) for i in order.__table__.columns})
    return dict_list

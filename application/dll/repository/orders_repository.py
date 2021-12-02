from application.dll.db import session
from application.dll.models import Orders


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



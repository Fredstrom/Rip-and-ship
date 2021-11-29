from application.dll.db import session
from application.dll.models import Customers


def create_customer(customer):
    customer = Customers(**customer)
    session.add(customer)
    session.commit()


def remove_customer(_id):
    customer = session.query(Customers).filter(Customers.customer_id == _id).first()
    session.delete(customer)
    session.commit()


def update_customer(_id, column, update):
    session.query(Customers).filter(Customers.customer_id == _id).update({column: update})
    session.commit()

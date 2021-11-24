from application.dll.db import session
from application.dll.models import Customers


def create_customer(customer):
    customer = Customers(**customer)
    session.add(customer)
    session.commit()

from application.dll.db import session
from application.dll.models import OrderDetails


def create_orderdetails(orderdetails):
    orderdetails = OrderDetails(**orderdetails)
    session.add(orderdetails)
    session.commit()

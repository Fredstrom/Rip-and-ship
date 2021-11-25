from application.dll.db import session
from application.dll.models import Orders


def create_orders(orders):
    orders = Orders(**orders)
    session.add(orders)
    session.commit()

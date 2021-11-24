from application.dll.db import session
from application.dll.models import Products


def create_product(product):
    products = Products(**product)
    session.add(products)
    session.commit()

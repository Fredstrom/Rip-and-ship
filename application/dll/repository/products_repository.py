from application.dll.db import session
from application.dll.models import Products


def create_product(product):
    products = Products(**product)
    session.add(products)
    session.commit()

def get_all_products():
    return session.query(Products).all()
from application.dll.db import session
from application.dll.models import Products


def create_product(product):
    products = Products(**product)
    session.add(products)
    session.commit()


def get_all_products():
    return session.query(Products).all()


def remove_product(_id):
    product = session.query(Products).filter(Products.product_id == _id).first()
    session.delete(product)
    session.commit()


def update_product(_id, column, update):
    session.query(Products).filter(Products.employee_id == _id).update({column: update})
    session.commit()

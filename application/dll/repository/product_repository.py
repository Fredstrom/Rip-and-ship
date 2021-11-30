import re
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


def get_product_by_id(_id):
    return session.query(Products).filter(Products.product_id == _id).first()


def order_by_product(column):
    return [{
                'product_id': product.product_id,
                'product_name': product.product_name,
                'description': product.description,
                'price_in': product.price_in
            } for product in session.query(Products).order_by(column)]


def search_for_product(column, search_for):
    products = session.query(Products).all()
    return [{
                'product_id': product.product_id,
                'product_name': product.product_name,
                'description': product.description,
                'price_in': product.price_in
            } for product in products if re.search(search_for, getattr(product, column))]


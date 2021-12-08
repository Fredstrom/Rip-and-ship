import re

from application.dll.mongo.models.sub_models import Product


def create_product(manufacturer, supplier, product):
    if manufacturer:
        product['manufacturer'] = []
        for i in manufacturer:
            product['manufacturer'].append(i)
    if supplier:
        product['supplier'] = []
        for i in supplier:
            product['supplier'].append(i)
    product = Product(**product)
    product.save()


def remove_product(_id: int):
    product = Product.find(_id=_id).first()
    product.delete()


def update_product(_id: int, column: str, update):
    product = Product.find(_id=_id).first()
    product = Product(**product.__dict__)
    product.__setattr__(column, update)
    product.save()


def order_by_product(column: str) -> list:
    return [product for product in Product.order_by(column)]


def search_for_product(column: str, search_for) -> list:
    return [product.__dict__ for product in Product.get_all() if re.search(search_for, getattr(Product, column))]


def get_all_products() -> list:
    return [product.__dict__ for product in Product.get_all()]

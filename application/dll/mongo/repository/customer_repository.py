import re

import pymongo

from application.dll.mongo.models.sub_models import Customer


def create_customer(customer: dict, orders=None):
    if orders:
        customer['orders'] = [order for order in orders]
    customer = Customer(customer)
    customer.save()


def remove_customer(_id):
    customer = Customer.find(_id=_id).first()


def update_customer(column: str, update, _id):
    customer = Customer.find(_id=_id).first()
    customer = Customer(customer.__dict__)
    customer.__setattr__(column, update)
    customer.save()


def order_by_customer(column: str) -> list:
    return [customer for customer in Customer.order_by(column)]


def search_for_customer(column: str, search_for) -> list:
    return [customer.__dict__ for customer in Customer.get_all() if re.search(search_for, getattr(customer, column))]


def get_all_customers() -> list:
    return [customer.__dict__ for customer in Customer.get_all()]


def get_customer_by_id(**kwargs) -> list:
    return Customer.get_object_id(**kwargs)


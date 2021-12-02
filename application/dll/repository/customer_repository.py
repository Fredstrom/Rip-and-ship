from application.dll.db import session
from application.dll.models import Customers

import re


def create_customer(customer: dict):
    customer = Customers(**customer)
    session.add(customer)
    session.commit()


def remove_customer(_id: int):
    customer = session.query(Customers).filter(Customers.customer_id == _id).first()
    session.delete(customer)
    session.commit()


def update_customer(_id: int, column: str, update: str):
    session.query(Customers).filter(Customers.customer_id == _id).update({column: update})
    session.commit()


def get_customer_by_id(_id):
    customer = session.query(Customers).filter(Customers.customer_id == _id).first()
    return {i.name: getattr(customer, i.name) for i in customer.table.columns}


def order_by_customer(column: str):
    return [{
                'customer_id': customer.customer_id,
                'company_name': customer.company_name,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'address': customer.address,
                'city': customer.city,
                'zip_code': customer.zip_code,
                'phone': customer.phone,
                'email': customer.email
            } for customer in session.query(Customers).order_by(column)]


def search_for_customer(column: str, search_for: str):
    customers = session.query(Customers).all()
    return [{
                'customer_id': customer.customer_id,
                'company_name': customer.company_name,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'address': customer.address,
                'city': customer.city,
                'zip_code': customer.zip_code,
                'phone': customer.phone,
                'email': customer.email
            } for customer in customers if re.search(search_for, getattr(customer, column))]

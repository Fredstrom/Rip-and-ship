import re

from application.dll.db import session
from application.dll.models import Suppliers


def create_suppliers(supplier: dict):
    supplier = Suppliers(**supplier)
    session.add(supplier)
    session.commit()


def remove_supplier(_id: int):
    contact_person = session.query(Suppliers).filter(Suppliers.supplier_id == _id).first()
    session.delete(contact_person)
    session.commit()


def update_supplier(_id: int, column: str, update: str):
    session.query(Suppliers).filter(Suppliers.supplier_id == _id).update({column: update})
    session.commit()


def order_by_supplier(column: str):
    return [{
                'supplier_id': supplier.supplier_id,
                'company_name': supplier.company_name,
                'address': supplier.address,
                'city': supplier.city,
                'zip_code': supplier.zip_code,
                'contact_id': supplier.contact_id
            } for supplier in session.query(Suppliers).order_by(column)]


def search_for_supplier(column: str, search_for: str):
    suppliers = session.query(Suppliers).all()
    return [{
                'supplier_id': supplier.supplier_id,
                'company_name': supplier.company_name,
                'address': supplier.address,
                'city': supplier.city,
                'zip_code': supplier.zip_code,
                'contact_id': supplier.contact_id
            } for supplier in suppliers if re.search(search_for, getattr(supplier, column))]

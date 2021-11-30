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

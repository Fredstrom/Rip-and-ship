from application.dll.db import session
from application.dll.models import Suppliers


def create_suppliers(supplier):
    supplier = Suppliers(**supplier)
    session.add(supplier)
    session.commit()

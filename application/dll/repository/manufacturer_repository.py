import re

from application.dll.db import session
from application.dll.models import Manufacturers


def create_manufacturer(manufacturer):
    manufacturer = Manufacturers(**manufacturer)
    session.add(manufacturer)
    session.commit()


def remove_manufacturer(_id):
    manufacturer = session.query(Manufacturers).filter(Manufacturers.manufacturer_id == _id).first()
    session.delete(manufacturer)
    session.commit()


def update_manufacturer(_id, column, update):
    session.query(Manufacturers).filter(Manufacturers.manufacturer_id == _id).update({column: update})
    session.commit()


def get_manufacturer_by_id(_id):
    manufacturer = session.query(Manufacturers).filter(Manufacturers.manufacturer_id == _id).first()
    return {i.name: getattr(manufacturer, i.name) for i in manufacturer.table.columns}


def order_by_manufacturer(column):
    return [{
        'manufacturer_id': manufacturer.manufacurer_id,
        'company_name': manufacturer.company_name,
        'address': manufacturer.address,
        'city': manufacturer.city,
        'zip_code': manufacturer.zip_code,
        'phone': manufacturer.phone,
        'contact_id': manufacturer.contact_id
    } for manufacturer in session.query(Manufacturers).order_by(column)]


def search_for_manufacturer(column, search_for):
    manufacturers = session.query(Manufacturers).all()
    return [{
        'manufacturer_id': manufacturer.manufacurer_id,
        'company_name': manufacturer.company_name,
        'address': manufacturer.address,
        'city': manufacturer.city,
        'zip_code': manufacturer.zip_code,
        'phone': manufacturer.phone,
        'contact_id': manufacturer.contact_id
    } for manufacturer in manufacturers if re.search(search_for, getattr(manufacturer, column))]

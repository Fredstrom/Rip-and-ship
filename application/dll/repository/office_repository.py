import re

from application.dll.db import session
from application.dll.models import Offices


def create_office(offices):
    office = Offices(**offices)
    session.add(office)
    session.commit()


def remove_office(_id):
    office = session.query(Offices).filter(Offices.store_id == _id).first()
    session.delete(office)
    session.commit()


def update_office(_id, column, update):
    session.query(Offices).filter(Offices.store_id == _id).update({column: update})
    session.commit()


def get_office_by_id(_id):
    return session.query(Offices).filter(Offices.store_id == _id).first()


def order_by_office(column):
    return [{
                'store_id': office.store_id,
                'name': office.name,
                'address': office.address,
                'zip_code': office.zip_code,
                'phone': office.phone
            } for office in session.query(Offices).order_by(column)]


def search_for_office(column, search_for):
    offices = session.query(Offices).all()
    return [{
                'store_id': office.store_id,
                'name': office.name,
                'address': office.address,
                'zip_code': office.zip_code,
                'phone': office.phone
            } for office in offices if re.search(search_for, getattr(office, column))]
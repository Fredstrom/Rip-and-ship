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
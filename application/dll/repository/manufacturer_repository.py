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
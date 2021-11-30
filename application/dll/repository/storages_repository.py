from application.dll.db import session
from application.dll.models import Storages


def create_storages(storage: dict):
    storage = Storages(**storage)
    session.add(storage)
    session.commit()


def remove_storage(_id: int):
    contact_person = session.query(Storages).filter(Storages.shelf_id == _id).first()
    session.delete(contact_person)
    session.commit()


def update_storage(_id: int, column: str, update: str):
    session.query(Storages).filter(Storages.shelf_id == _id).update({column: update})
    session.commit()

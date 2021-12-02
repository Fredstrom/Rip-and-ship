import re

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


def get_storage_by_id(_id):
    storage = session.query(Storages).filter(Storages.storage_id == _id).first()
    return {i.name: getattr(storage, i.name) for i in storage.table.columns}


def order_by_storage(column):
    return [{
                'shelf_id': storage.shelf_id,
                'units_in_stock': storage.units_in_stock,
                'capacity': storage.capacity,
                'product_id': storage.product_id
            } for storage in session.query(Storages).order_by(column)]


def search_for_storage(column, search_for):
    storages = session.query(Storages).all()
    return [{
                'shelf_id': storage.shelf_id,
                'units_in_stock': storage.units_in_stock,
                'capacity': storage.capacity,
                'product_id': storage.product_id
            } for storage in storages if re.search(search_for, getattr(storage, column))]


def get_all_storages():
    storages = session.query(Storages).all()
    dict_list = []
    for storage in storages:
        dict_list.append({i.name: getattr(storage, i.name) for i in storage.__table__.columns})
    return dict_list

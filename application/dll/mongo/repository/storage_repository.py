import re
from application.dll.mongo.models.sub_models import Storage


def create_storage(storage: dict):
    storage = Storage(**storage)
    storage.save()


def remove_storage(_id: int):
    storage = Storage.find(_id=_id).first()
    storage.delete()


def update_storage(_id: int, column: str, update):
    storage = Storage.find(_id=_id).first()
    storage = Storage(**storage.__dict__)
    storage.__setattr__(column, update)
    storage.save()


def order_by_storage(column: str) -> list:
    return [storage for storage in Storage.order_by(column)]


def search_for_storage(column: str, search_for) -> list:
    return [storage.__dict__ for storage in Storage.get_all() if re.search(search_for, getattr(storage, column))]


def get_all_storages() -> list:
    return [storage.__dict__ for storage in Storage.get_all()]

from application.dll.db import session
from application.dll.models import Storages


def create_storages(storage):
    storage = Storages(**storage)
    session.add(storage)
    session.commit()

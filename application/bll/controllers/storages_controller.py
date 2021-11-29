from application.dll.repository import storages_repository


def create_storages(storage: dict):
    storages_repository.create_storages(storage)


def remove_customer(_id: int):
    storages_repository.remove_storage(_id)


def update_customer(_id: int, column: str, update: str):
    storages_repository.update_storage(_id, column, update)
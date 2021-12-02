from application.dll.repository import storage_repository


def create_storages(storage: dict):
    storage_repository.create_storages(storage)


def remove_customer(_id: int):
    storage_repository.remove_storage(_id)


def update_customer(_id: int, column: str, update: str):
    storage_repository.update_storage(_id, column, update)

def get_storage_by_id(_id):
    return storage_repository.get_storage_by_id(_id)


def order_by_storage(column):
    return storage_repository.order_by_storage(column)


def search_for_storage(column, search_for):
    return storage_repository.search_for_storage(column, search_for)


def get_all_storages():
    storage_repository.get_all_storages()

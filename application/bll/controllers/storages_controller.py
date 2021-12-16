from application.dll.mongo.repository import storage_repository


def create_storage(storage: dict):
    storage_repository.create_storage(storage)


def remove_storage(**kwargs):
    storage_repository.remove_storage(**kwargs)


def update_storage(column: str, update, _id):
    storage_repository.update_storage(column, update, _id)


def get_storage_by_id(**kwargs) -> list:
    return storage_repository.get_storage_by_id(**kwargs)


def order_by_storage(column: str) -> list:
    return storage_repository.order_by_storage(column)


def search_for_storage(column: str, search_for: str) -> list:
    return storage_repository.search_for_storage(column, search_for)


def get_all_storages() -> list:
    return storage_repository.get_all_storages()



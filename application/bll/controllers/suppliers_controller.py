from application.dll.repository import suppliers_repository


def create_suppliers(supplier: dict):
    suppliers_repository.create_suppliers(supplier)


def remove_customer(_id: int):
    suppliers_repository.remove_supplier(_id)


def update_customer(_id: int, column: str, update: str):
    suppliers_repository.update_supplier(_id, column, update)

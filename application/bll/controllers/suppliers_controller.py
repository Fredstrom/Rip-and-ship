from application.dll.repository import suppliers_repository


def create_suppliers(supplier: dict):
    suppliers_repository.create_suppliers(supplier)


def remove_supplier(_id: int):
    suppliers_repository.remove_supplier(_id)


def update_supplier(_id: int, column: str, update: str):
    suppliers_repository.update_supplier(_id, column, update)


def get_supplier_by_id(_id):
    return suppliers_repository.get_supplier_by_id(_id)


def order_by_supplier(column: str):
    suppliers_repository.order_by_supplier(column)


def search_for_supplier(column: str, search_for: str):
    suppliers_repository.search_for_supplier(column, search_for)

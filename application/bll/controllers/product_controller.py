from application.dll.mongo.repository import product_repository


def create_product(product: dict):
    product_repository.create_product(product)


def remove_product(**kwargs):
    product_repository.remove_product(**kwargs)


def update_product(column: str, update, _id):
    product_repository.update_product(column, update, _id)


def get_product_by_id(**kwargs) -> list:
    return product_repository.get_product_by_id(**kwargs)


def order_by_product(column: str) -> list:
    return product_repository.order_by_product(column)


def search_for_product(column: str, search_for: str) -> list:
    return product_repository.search_for_product(column, search_for)


def get_all_product() -> list:
    return product_repository.get_all_products()

from application.dll.repository import products_repository


def create_product(product):
    products_repository.create_product(product)

def get_all_product():
    return products_repository.get_all_products()

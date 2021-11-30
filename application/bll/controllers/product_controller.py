from application.dll.repository import product_repository


def create_product(product):
    product_repository.create_product(product)

def get_all_product():
    return product_repository.get_all_products()

def remove_product(_id):
    product_repository.remove_product(_id)


def update_product(_id, column, update):
    product_repository.update_product(_id, column, update)


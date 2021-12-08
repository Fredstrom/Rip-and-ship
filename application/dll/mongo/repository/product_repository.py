from application.dll.mongo.models.sub_models import Product


def create_product(manufacturer, supplier, product):
    if manufacturer:
        product['manufacturer'] = manufacturer
    if supplier:
        product['supplier'] = supplier
    product = Product(**product)
    product.save()

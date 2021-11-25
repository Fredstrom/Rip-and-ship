from application.dll.db import session
from application.dll.models import ProductsFitModels


def create_products_fit_models(product_fit_model):
    product_fit_model = ProductsFitModels(**product_fit_model)
    session.add(product_fit_model)
    session.commit()

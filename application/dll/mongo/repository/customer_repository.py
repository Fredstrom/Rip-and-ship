from application.dll.mongo.models.sub_models import Customer


def create_customer(customer: dict):
    customer = Customer(**customer)
    customer.save()


def remove_customer(_id):
    customers = Customer.find(_id=_id)
    for customer in customers:
        customer.delete()


# def search_for_customer(column: str, search_for: str) -> list:
#     return Customer.find(column=search_for).first()


def get_all_customers() -> list:
    return Customer.get_all()


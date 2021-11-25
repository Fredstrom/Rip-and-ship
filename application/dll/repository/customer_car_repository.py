from application.dll.db import session
from application.dll.models import CustomerCarsModels


def create_customer_car(customer_car):
    customer_car = CustomerCarsModels(**customer_car)
    session.add(customer_car)
    session.commit()

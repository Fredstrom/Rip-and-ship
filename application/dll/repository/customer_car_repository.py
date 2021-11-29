from application.dll.db import session
from application.dll.models import CustomerCarsModels


def create_customer_car(customer_car: dict):
    customer_car = CustomerCarsModels(**customer_car)
    session.add(customer_car)
    session.commit()


def remove_customer_car(vin_no: str):
    contact_person = session.query(CustomerCarsModels).filter(CustomerCarsModels.vin_no == vin_no).first()
    session.delete(contact_person)
    session.commit()


def update_customer_car(vin_no: str, column: str, update: str):
    session.query(CustomerCarsModels).filter(CustomerCarsModels.vin_no == vin_no).update({column: update})
    session.commit()

from application.dll.db import session
from application.dll.models import CustomerCarsModels
import re

def create_customer_car(customer_car: dict):
    customer_car = CustomerCarsModels(**customer_car)
    session.add(customer_car)
    session.commit()


def remove_customer_car(vin_no: str):
    customer_car = session.query(CustomerCarsModels).filter(CustomerCarsModels.vin_no == vin_no).first()
    session.delete(customer_car)
    session.commit()


def update_customer_car(vin_no: str, column: str, update: str):
    session.query(CustomerCarsModels).filter(CustomerCarsModels.vin_no == vin_no).update({column: update})
    session.commit()


def get_customer_car_by_id(vin_no):
    customer_car = session.query(CustomerCarsModels).filter(CustomerCarsModels.vin_no == vin_no).first()
    return {i.name: getattr(customer_car, i.name) for i in customer_car.table.columns}


def order_by_customer_car(column: str):
    return [{
                'vin_no': car.vin_no,
                'customer_id': car.customer_id,
                'color': car.color,
                'year': car.year,
                'model': car.model,
                'brand': car.brand
            } for car in session.query(CustomerCarsModels).order_by(column)]


def search_for_customer_car(column: str, search_for: str):
    cars = session.query(CustomerCarsModels).all()
    return [{
                'vin_no': car.vin_no,
                'customer_id': car.customer_id,
                'color': car.color,
                'year': car.year,
                'model': car.model,
                'brand': car.brand
            } for car in cars if re.search(search_for, getattr(car, column))]

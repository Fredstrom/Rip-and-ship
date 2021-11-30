from application.dll.repository import customer_car_repository


def create_customer_car(customer_car: dict):
    customer_car_repository.create_customer_car(customer_car)


def remove_customer_car(_id: int):
    customer_car_repository.remove_customer_car(_id)


def update_customer_car(vin_no: str, column: str, update: str):
    customer_car_repository.update_customer_car(vin_no, column, update)

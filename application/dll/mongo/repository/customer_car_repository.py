from application.dll.mongo.models.sub_models import CarModel


def create_customer_car(compatible_products: list, customer_car: dict):
    if compatible_products:
        customer_car['compatible_products'] = []
        for product in compatible_products:
            customer_car['compatible_products'].append(product)
    customer_car = CarModel(**customer_car)
    customer_car.save()


# def remove_customer_car(vin_no: str):
#     CarModel.delete()


def update_customer_car(vin_no: str, column: str, update: str):
    car = CarModel.find(vin_no=vin_no).first()
    car = CarModel(**car.__dict__)
    car.__setattr__(column, update)
    car.save()


def get_customer_car_by_id(vin_no: str) -> dict:
    return CarModel.find(vin_no=vin_no).first().__dict__


# def order_by_customer_car(column: str) -> list:
#     return [{
#                 'vin_no': car.vin_no,
#                 'customer_id': car.customer_id,
#                 'color': car.color,
#                 'year': car.year,
#                 'model': car.model,
#                 'brand': car.brand
#             } for car in CarModel.order_by(column)]


def search_for_customer_cars(column: str, search_for: str,) -> list:
    return CarModel.find(column=search_for).first()


def get_all_customer_cars() -> list:
    return [car.__dict__ for car in CarModel.get_all()]


print(get_all_customer_cars())

import datetime
import random

from application.dll.mongo.repository import customer_car_repository, customer_repository, employee_repository,\
    product_repository, storage_repository

import json

with open('generator/data_files/cars.json', 'r', encoding='utf-8') as file:
    cars = json.load(file)

with open('generator/data_files/contact_persons.json', 'r', encoding='utf-8') as file:
    contact_persons = json.load(file)

with open('generator/data_files/customers.json', 'r', encoding='utf-8') as file:
    customers = json.load(file)

with open('generator/data_files/employees.json', 'r', encoding='utf-8') as file:
    employees = json.load(file)

with open('generator/data_files/manufacturers.json', 'r', encoding='utf-8') as file:
    manufacturers = json.load(file)

with open('generator/data_files/products.json', 'r', encoding='utf-8') as file:
    products = json.load(file)

with open('generator/data_files/offices.json', 'r', encoding='utf-8') as file:
    offices = json.load(file)

with open('generator/data_files/suppliers.json', 'r', encoding='utf-8') as file:
    suppliers = json.load(file)


def generate_order_dates(start, end):
    start_year, start_month, start_day = start.split('-')
    end_year, end_month, end_day = end.split('-')

    start = datetime.datetime(int(start_year), int(start_month), int(start_day))
    end = datetime.datetime(int(end_year), int(end_month), int(end_day))
    dates = []
    delivery = []

    for i in range(500):
        time_between_dates = end - start
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)

        dates.append(start + datetime.timedelta(days=random_number_of_days, hours=random.randrange(0, 12)
                                                , minutes=random.randrange(0, 60), seconds=random.randrange(0, 60)))

        delivery.append(dates[i] + datetime.timedelta(days=dates[i].day + 5 if dates[i].day + 5 < 28 else 5,
                                                      hours=dates[i].hour, minutes=dates[i].minute,
                                                      seconds=dates[i].second))

    return dates, delivery


def create_order_details():
    return [{
            'product_id': None,
            'quantity': random.randrange(1, 20),
            'price_each': random.randrange(20, 2000)
        } for _ in range(random.randrange(0, 5))]


def create_order_dict(order_date, delivery_date):
    return {
        'order_date': order_date,
        'delivery_date': delivery_date,
        'employee_id': None,
        'order_details': [od for od in create_order_details()]
    }


def create_contact_persons(first_name, last_name, email, phone):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone
    }


def create_manufacturer(company_name, address, city, zip_code, contact_person):
    return {
        'company_name': company_name,
        'address': address,
        'city': city,
        'zip_code': zip_code,
        'contact_person': contact_person
    }


def create_supplier(company_name, address, city, zip_code, contact_person):
    return {
        'company_name': company_name,
        'address': address,
        'city': city,
        'zip_code': zip_code,
        'contact_person': contact_person
    }


def create_offices(name, address, zip_code, phone):
    return {
        'name': name,
        'address': address,
        'zip_code': zip_code,
        'phone': phone
    }


def create_storages(capacity):
    return {
        'units_in_stock': random.randrange(0, capacity),
        'capacity': capacity,
        'product_id': None
    }


def main():
    order_dates, delivery_dates = generate_order_dates('2000-01-01', '2022-01-01')
    od = []
    for i in range(len(order_dates)):
        od.append(create_order_dict(order_dates[i], delivery_dates[i]))

    c_p =[]
    man = []
    supp = []
    off = []
    for i in range(len(contact_persons)):
        c_p.append(create_contact_persons(contact_persons[i]['first_name'], contact_persons[i]['last_name'], contact_persons[i]['email'], contact_persons[i]['phone']))

    for i in range(len(manufacturers)):
        man.append(create_manufacturer(manufacturers[i]['company_name'], manufacturers[i]['address'], manufacturers[i]['city'], manufacturers[i]['zip_code'], random.choice(c_p)))

    for i in range(len(suppliers)):
        supp.append(create_supplier(suppliers[i]['company_name'], suppliers[i]['address'], suppliers[i]['city'], suppliers[i]['zip_code'], random.choice(c_p)))

    for i in range(len(offices)):
        off.append(create_offices(offices[i]['name'], offices[i]['address'], offices[i]['zip_code'], offices[i]['phone']))

    for i in range(len(customers)):
        customer_repository.create_customer([random.choice(od) for _ in range(random.randrange(1, 10))], customers[i])

    for i in range(len(products)):
        product_repository.create_product([random.choice(man) for _ in range(random.randrange(1, 3))],
                                                    [random.choice(supp) for _ in range(random.randrange(1, 2))], products[i])

    for i in range(len(cars)):
        customer_car_repository.create_customer_car([random.choice(products) for _ in range(random.randrange(1, 20))], cars[i])

    for i in range(len(employees)):
        employee_repository.create_employee(random.choice(off), employees[i])

    for _ in range(200):
        storage_repository.create_storage(create_storages(random.randrange(10, 100)))


if __name__ == '__main__':
    main()

import random

from application.bll.controllers import customer_controller
from generator.json_to_list import customers


def generate_customers():
    for i in range(len(customers)):
        customer = {
            'company_name': customers[i]['company_name'],
            'first_name': customers[i]['first_name'],
            'last_name': customers[i]['last_name'],
            'address': customers[i]['address'],
            'city': customers[i]['city'],
            'zip_code': customers[i]['zip_code'],
            'phone': customers[i]['phone'],
            'email': customers[i]['email']
        }
        customer_controller.create_customer(customer)


def main():
    generate_customers()


if __name__ == '__main__':
    main()

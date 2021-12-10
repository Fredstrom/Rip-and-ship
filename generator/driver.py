import datetime

from application.dll.mysql_db.db import session
from application.dll.mysql_db.models import Product, Manufacturer, ContactPerson, Supplier, CarModel, Customer, \
    Employee, Office, Order, OrderDetail, OrderFromManufacturer, OrderFromSupplier, ProductFitsModel, Storage
import application.dll.mongo.models.sub_models as mm



def contact_persons():
    contact = []
    contact_persons = session.query(ContactPerson).all()
    for contact_person in contact_persons:
        as_dict = contact_person.__dict__
        del as_dict['_sa_instance_state']
        contact.append(as_dict)
    return contact


def pro_car():
    pro_car = []
    procars = session.query(ProductFitsModel).all()
    for procar in procars:
        as_dict = procar.__dict__
        del as_dict['_sa_instance_state']
        pro_car.append(as_dict)
    return pro_car


def customer_car():

    cars = session.query(CarModel).all()
    for car in cars:
        as_dict = car.__dict__
        del as_dict['_sa_instance_state']
        as_dict['owner'] = mm.Customer.find(customer_id=car.customer_id).first()._id
        as_dict['compatible_products'] = []
        for pc in pro_car():
            if car['vin_no'] == pc['vin_no']:
                as_dict['compatible_products'].append(mm.Product.find(product_id=pc['product_id']).first()._id)
        mongo_car = mm.CarModel(as_dict)
        mongo_car.save()


def customers():
    customers = session.query(Customer).all()
    for customer in customers:
        as_dict = customer.__dict__
        del as_dict['_sa_instance_state']
        if not as_dict['company_name']:
            del as_dict['company_name']
        as_dict['orders'] = []
        for order in orders():
            if order['customer_id'] == as_dict['customer_id']:
                as_dict['orders'].append(order)
        if len(as_dict['orders']) < 0:
            del as_dict['orders']
        mongo_customer = mm.Customer(as_dict)
        mongo_customer.save()


def offices():
    off = []
    offices = session.query(Office).all()
    for office in offices:
        as_dict = office.__dict__
        del as_dict['_sa_instance_state']
        off.append(as_dict)
        print()
    return off


def employees():
    employees = session.query(Employee).all()
    for employee in employees:
        as_dict = employee.__dict__
        del as_dict['_sa_instance_state']
        for office in offices():
            if office['store_id'] == as_dict['store_id']:
                as_dict['office'] = office
                break
        if not as_dict['office']:
            del as_dict['office']
        mongo_employee = mm.Employee(as_dict)
        mongo_employee.save()


def order_details():
    od = []
    details = session.query(OrderDetail).all()
    for detail in details:
        as_dict = detail.dict
        del as_dict['_sa_instance_state']
        as_dict['product'] = mm.Product.find(product_id=as_dict['produt_id']).first._id
        od.append(as_dict)
    return od



def orders():
    ord = []
    orders = session.query(Order).all()
    for order in orders:
        as_dict = order.__dict__
        del as_dict['_sa_instance_state']
        as_dict['employee'] = mm.Employee.find(employee_id = as_dict['employee_id']).first()._id
        as_dict['order_date'] = datetime.datetime(order.order_date.year, order.order_date.month, order.order_date.day)
        as_dict['delivery_date'] = datetime.datetime(order.delivery_date.year, order.order_date.month, order.order_date.day)
        as_dict['order_details'] = [od for od in order_details()]
        ord.append(as_dict)
    return ord








def manufacturers():
    man = []
    manufacturers = session.query(Manufacturer).all()
    for manufacturer in manufacturers:
        as_dict = manufacturer.__dict__
        del as_dict['_sa_instance_state']
        for contact in contact_persons():
            if contact['contact_id'] == as_dict['contact_id']:
                as_dict["contact_person"] = contact
                break
        man.append(as_dict)
    return man


def suppliers():
    supp = []
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        as_dict = supplier.__dict__
        del as_dict['_sa_instance_state']
        for contact in contact_persons():
            if contact['contact_id'] == as_dict['contact_id']:
                as_dict["contact_person"] = contact
                break
        supp.append(as_dict)
    return supp


def man_pro():
    man_pro = []
    manpros =session.query(OrderFromManufacturer).all()
    for manpro in manpros:
        as_dict = manpro.__dict__
        del as_dict['_sa_instance_state']
        man_pro.append(as_dict)
    return man_pro


def supp_pro():
    man_pro = []
    manpros = session.query(OrderFromSupplier).all()
    for manpro in manpros:
        as_dict = manpro.__dict__
        del as_dict['_sa_instance_state']
        man_pro.append(as_dict)
    return man_pro



def convert_products():
    products = session.query(Product).all()
    for product in products:
        as_dict = product.__dict__
        if 'description' not in as_dict:
            del as_dict['description']
        del as_dict['_sa_instance_state']
        as_dict['manufacturers'] = []
        as_dict['suppliers'] = []
        for manufacturer in manufacturers():
            for mp in man_pro():
                if manufacturer['manufacturer_id'] == mp['manufacturer_id'] and as_dict['product_id'] == mp['product_id']:
                    as_dict['manufacturers'].append(manufacturer)
                    break
        for supplier in suppliers():
            for sp in supp_pro():
                if supplier['supplier_id'] == sp['supplier_id'] and as_dict['product_id'] == sp['product_id']:
                    as_dict['suppliers'].append(supplier)
                    break


def storages():
    storages = session.query(Storage).all()
    for storage in storages:
        as_dict = storage.__dict__
        del as_dict['_sa_instance_state']
        del as_dict['TRIGGERS']
        as_dict['product'] = mm.Product.find(product_id=as_dict['product_id']).first()._id
        mongo_storage = mm.Storage(as_dict)
        mongo_storage.save()





def main():
    # convert_products()
    # contact_persons()
    # manufacturer()
    # customer_car()
    # customer()
    # employees()
    # offices()
    # orders()

if __name__ == '__main__':
    main()
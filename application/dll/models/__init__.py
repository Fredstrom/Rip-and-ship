from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from application.dll.db import Base


class CustomerCarsModels(Base):
    __tablename__ = 'customer_cars_models'

    vin_no = Column(Integer, primary_key=True, unique=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    color = Column(String(45), nullable=False)
    year = Column(Integer, nullable=False)
    model = Column(String(45), nullable=False)
    brand = Column(String(45), nullable=False)


class ContactPersons(Base):
    __tablename__ = 'contact_persons'

    contact_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)


class Customers(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(45), nullable=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)


class Employees(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    store_id = Column(Integer, ForeignKey('offices.store_id'))
    offices = relationship('Offices')


class Manufacturers(Base):
    __tablename__ = 'manufacturers'

    manufacturer_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact_persons.contact_id'))
    contact_persons = relationship('Contact_persons')


class Offices(Base):
    __tablename__ = 'offices'

    store_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)


class OrderDetails(Base):
    __tablename__ = 'orderdetails'

    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price_each = Column(Integer, nullable=False)
    orders = relationship('Orders')
    products = relationship('Products')


class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    delivery_date = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    employee_id = Column(Integer, ForeignKey('employee.employee_id'))
    buy_datetime = Column(DateTime, nullable=False)
    customers = relationship('Customers')
    employee = relationship('Employees')


class Products(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(45), nullable=False)
    description = Column(String(45), nullable=False)
    price_in = Column(Integer, nullable=False)


class ProductsFitModels(Base):
    __tablename__ = 'products_fits_models'

    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    vin_no = Column(Integer, ForeignKey('customer_cars_models.vin_no'), primary_key=True)
    products = relationship('Products')
    cars = relationship('Customer_cars_models')


class OrdersFromManufacturers(Base):
    __tablename__ = 'orders_from_manufacturers'

    manufacturers_id = Column(Integer, ForeignKey('manufacturers.manufacturer_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    products = relationship('Products')
    manufacturers = relationship('Manufacturers')


class OrdersFromSuppliers(Base):
    __tablename__ = 'orders_from_suppliers'

    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    products = relationship('Products')
    suppliers = relationship('Suppliers')


class Storages(Base):
    __tablename__ = 'storages'

    shelf_id = Column(Integer, primary_key=True, autoincrement=True)
    units_in_stock = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    buy_price = Column(Integer, nullable=False)
    TRIGGERS = Column(String(45), nullable=True)
    products_id = Column(Integer, ForeignKey('products.product_id'))
    products = relationship('Products')


class Suppliers(Base):
    __tablename__ = 'suppliers'

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact_persons.contact_id'))
    contact_persons = relationship('Contact_persons')


class SuppliersOrdersFrom(Base):
    __tablename__ = 'suppliers_orders_from'

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.manufacturer_id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'))
    manufacturer = relationship('Manufacturers')
    suppliers = relationship('Suppliers')

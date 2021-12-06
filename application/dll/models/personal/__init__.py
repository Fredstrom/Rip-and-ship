from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db import Base


class ContactPerson(Base):
    __tablename__ = 'contact_persons'

    contact_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    manufacturer = relationship('application.dll.models.company.Manufacturer', back_populates='contact_persons')
    supplier = relationship('application.dll.models.company.Supplier', back_populates='contact_persons')


class Customer(Base):
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
    cars = relationship('application.dll.models.car_and_product.CarModel', back_populates='customer')
    orders = relationship('application.dll.models.order.Order', back_populates='customer')


class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    store_id = Column(Integer, ForeignKey('offices.store_id'))
    offices = relationship('application.dll.models.company.Office', back_populates='employee')
    orders = relationship('application.dll.models.order.Order', back_populates='employee')



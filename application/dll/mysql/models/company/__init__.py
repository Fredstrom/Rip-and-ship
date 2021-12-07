from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.mysql.db import Base


class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    manufacturer_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact_persons.contact_id'))
    contact_persons = relationship('application.dll.models.personal.ContactPerson', back_populates='manufacturer')


class Office(Base):
    __tablename__ = 'offices'

    store_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    employee = relationship('application.dll.models.personal.Employee', back_populates='offices')


class Storage(Base):
    __tablename__ = 'storages'

    shelf_id = Column(Integer, primary_key=True, autoincrement=True)
    units_in_stock = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    TRIGGERS = Column(String(45), nullable=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    products = relationship('application.dll.models.car_and_product.Product')


class Supplier(Base):
    __tablename__ = 'suppliers'

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)
    city = Column(String(45), nullable=False)
    zip_code = Column(String(45), nullable=False)
    contact_id = Column(Integer, ForeignKey('contact_persons.contact_id'))
    contact_persons = relationship('application.dll.models.personal.ContactPerson', back_populates='supplier')



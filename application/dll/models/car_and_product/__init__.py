from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.dll.db import Base


class CarModel(Base):
    __tablename__ = 'customer_cars_models'

    vin_no = Column(Integer, primary_key=True, unique=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    color = Column(String(45), nullable=False)
    year = Column(Integer, nullable=False)
    model = Column(String(45), nullable=False)
    brand = Column(String(45), nullable=False)
    customer = relationship = relationship('application.dll.models.personal.Customer', back_populates='cars')


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(45), nullable=False)
    description = Column(String(45))
    price_in = Column(Integer, nullable=False)
    order_details = relationship('application.dll.models.order.OrderDetail', back_populates='products')


class ProductFitsModel(Base):
    __tablename__ = 'products_fits_models'

    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    vin_no = Column(Integer, ForeignKey('customer_cars_models.vin_no'), primary_key=True)
    products = relationship('application.dll.models.car_and_product.Product')
    cars = relationship('application.dll.models.car_and_product.CarModel')


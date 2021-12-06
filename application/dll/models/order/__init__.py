from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from application.dll.db import Base


class OrderDetail(Base):
    __tablename__ = 'orderdetails'

    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price_each = Column(Integer, nullable=False)
    orders = relationship('Order', back_populates='order_details')
    products = relationship('application.dll.models.car_and_product.Product', back_populates='order_details')


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    delivery_date = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    customer = relationship('application.dll.models.personal.Customer', back_populates='orders')
    employee = relationship('application.dll.models.personal.Employee', back_populates='orders')
    order_details = relationship('OrderDetail')


class OrderFromManufacturer(Base):
    __tablename__ = 'orders_from_manufacturers'

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.manufacturer_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    products = relationship('application.dll.models.car_and_product.Product')
    manufacturers = relationship('application.dll.models.company.Manufacturer')


class OrderFromSupplier(Base):
    __tablename__ = 'orders_from_suppliers'

    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    products = relationship('application.dll.models.car_and_model.Product')
    suppliers = relationship('application.dll.models.company.Supplier')


class SupplierOrdersFrom(Base):
    __tablename__ = 'suppliers_orders_from'

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.manufacturer_id'), primary_key=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), primary_key=True)
    manufacturer = relationship('application.dll.models.company.Manufacturer')
    suppliers = relationship('application.dll.models.company.Supplier')


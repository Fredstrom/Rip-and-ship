from application.dll.mongo.models import Document, db


class CarModel(Document):
    collection = db.car_models


class ContactPerson(Document):
    collection = db.contact_persons


class Customer(Document):
    collection = db.customers


class Employee(Document):
    collection = db.employees


class Manufacturer(Document):
    collection = db.manufacturers


class Office(Document):
    collection = db.offices


class Order(Document):
    collection = db.orders


class Product(Document):
    collection = db.products


class Storage(Document):
    collection = db.storages


class Supplier(Document):
    collection = db.suppliers

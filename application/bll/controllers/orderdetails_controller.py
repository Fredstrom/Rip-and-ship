from application.dll.repository import orderdetails_repository


def create_orderdetails(orderdetails):
    orderdetails_repository.create_orderdetails(orderdetails)

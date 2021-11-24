from application.dll.db import session
from application.dll.models import Employees


def create_employee(employee):
    employee = Employees(**employee)
    session.add(employee)
    session.commit()

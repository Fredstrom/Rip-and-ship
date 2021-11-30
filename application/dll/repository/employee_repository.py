from application.dll.db import session
from application.dll.models import Employees


def create_employee(employee):
    employee = Employees(**employee)
    session.add(employee)
    session.commit()


def remove_employee(_id):
    employees = session.query(Employees).filter(Employees.employee_id == _id).first()
    session.delete(employees)
    session.commit()


def update_employee(_id, column, update):
    session.query(Employees).filter(Employees.employee_id == _id).update({column: update})
    session.commit()



import re

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


def get_employee_by_id(_id):

    employee = session.query(Employees).filter(Employees.employee_id == _id).first()
    return {i.name: getattr(employee, i.name) for i in employee.table.columns}


def order_by_employee(column):
    return [{
        'employee_id': employee.manufacurer_id,
        'company_name': employee.company_name,
        'address': employee.address,
        'city': employee.city,
        'zip_code': employee.zip_code,
        'phone': employee.phone,
        'contact_id': employee.contact_id
    } for employee in session.query(Employees).order_by(column)]


def search_for_employee(column, search_for):
    employees = session.query(Employees).all()
    return [{
        'employee_id': employee.manufacurer_id,
        'company_name': employee.company_name,
        'address': employee.address,
        'city': employee.city,
        'zip_code': employee.zip_code,
        'phone': employee.phone,
        'contact_id': employee.contact_id
    } for employee in employees if re.search(search_for, getattr(employee, column))]


def get_all_employees():
    employees = session.query(Employees).all()
    dict_list = []
    for employee in employees:
        dict_list.append({i.name: getattr(employee, i.name) for i in employee.__table__.columns})
    return dict_list

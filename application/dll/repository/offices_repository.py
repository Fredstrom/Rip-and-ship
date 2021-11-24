from application.dll.db import session
from application.dll.models import Offices


def create_office(offices):
    office = Offices(**offices)
    session.add(office)
    session.commit()
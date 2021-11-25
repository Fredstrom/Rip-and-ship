from application.dll.db import session
from application.dll.models import Manufacturers


def create_manufacturer(manufacturer):
    manufacturer = Manufacturers(**manufacturer)
    session.add(manufacturer)
    session.commit()

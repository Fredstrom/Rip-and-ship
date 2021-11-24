import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker


engine = sqlalchemy.create_engine(
    f"mysql+mysqlconnector://root:Hej123@localhost:3306/Spare_partsDB"
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


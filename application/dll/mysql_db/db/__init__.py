import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from application.config.db_config import *


# engine = sqlalchemy.create_engine(
#     f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
# )

engine = sqlalchemy.create_engine(
    f"mysql+mysqlconnector://root:Hej123@localhost:33011/Rip-and-Ship"
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


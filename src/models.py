from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String


Base = declarative_base()


class Pokemon(Base):

    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), unique=True, nullable=False)
    sprite = Column(Text)
    height = Column(Integer)
    weight = Column(Integer)

from sqlalchemy.ext.declarative import declarative_base  # for defining the base class
from sqlalchemy import Column, Integer, String  # for defining columns and data types

Base = declarative_base()


# must have at least one columns
# the table must be provided via the attribute __tablename__
class Menu(Base):
    __tablename__ = 'menus'  # class attribute providing the table name

    id = Column(Integer, primary_key=True)  # primary key column
    name = Column(String())  # name column
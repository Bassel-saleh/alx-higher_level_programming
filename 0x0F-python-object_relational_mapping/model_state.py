#!/usr/bin/python3
""" State class and Base, an instance of declarative_base """
from sqlalchemy import Column, Integer, Nullable, String, MetaData, column
from sqlalchemy.ext.declarative import declarative_base
mymetadata = MetaData()
base = declarative_base(metadata=mymetadata)


class state(Base):
    """intiates state class which inherit from Base
    """
    __tablename__ = 'states'
    id = column(Integer, unique=True, nullable=False, primary_key=True)
    name = column(String(128), nullable=False)

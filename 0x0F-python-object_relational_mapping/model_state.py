#!/usr/bin/python3
""" Module creates a state class definition and Base instance """
from sqlalchemy import Column, Integer, String, Identity, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ definition of State class """

    __tablename__ = "states"
    id = Column(
      Integer, Identity(start=1, cycle=True), primary_key=True, nullable=False
    )
    name = Column(String(128), nullable=False)

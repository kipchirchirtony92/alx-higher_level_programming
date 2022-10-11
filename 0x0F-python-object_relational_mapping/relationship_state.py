#!/usr/bin/env python3
# Defines the state table in mysql hbtn_0e_100_usa db
# creates a table that has a relationship of one to many with the cities table
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ Represents a state table in hbtn_0e_100_usa db


    Attributes:
              id (sqlalchemy.Column) : the state id and primary key
              name(sqlalchemy.Column): the name if the state
              cities (sqlalchemy.Column) : the states-cities relationship
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=True)

    cities = relationship("City", backref="state", cascade="all, delete")

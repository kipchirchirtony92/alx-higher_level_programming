#!/usr/bin/env python3
# lists all City objects from the database hbtn_0e_101_usa
# Usage: ./102-relationship_cities_states_list.py <mysql username> /
#                                                 <mysql password> /
#                                                 <database name>
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import Base, City
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print(f"{city.id}: {city.name} -> {city.state.name}")

#!/usr/bin/env python3
# creates the Sate Carlifornia with the City San Francisco
# Usage: ./100-relationship_states_cityies.py : <mysql username>
#                                               <mysql password>
#                                                <database name>


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = City(name="San Fransisco", state=State(name="Carlifornia"))
    session.add(new_city)
    session.commit()

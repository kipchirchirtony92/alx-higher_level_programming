#!/usr/bin/python3
"""
list all State objects that contain the letter a from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s = '%a%'
    states = session.query(State).order_by(State.id)
    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
    session.close()

#!/usr/bin/python3
""" prints the State object with argument passed from the database """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    start = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(start)
    Session = sessionmaker(bind=start)
    session = Session()
    kd = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(kd[0].id)
    except IndexError:
        print("Not found")

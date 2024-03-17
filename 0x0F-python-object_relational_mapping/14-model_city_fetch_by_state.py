#!/usr/bin/python3
""" prints the State object with the argument from database """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    start = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(start)
    Session = sessionmaker(bind=start)
    session = Session()
    for kd in (session.query(State.name, City.id, City.name)
               .filter(State.id == City.state_id)):
        print(kd[0] + ": (" + str(kd[1]) + ") " + kd[2])

#!/usr/bin/python3
""" prints the State object with argument from the database """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
if __name__ == "__main__":
    start = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(start)
    Session = sessionmaker(bind=start)
    session = Session()
    for kd in session.query(State).order_by(State.id):
        print(kd.id, kd.name, sep=": ")
        for city_ins in kd.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")

#!/usr/bin/python3
""" Creates the State "California" with the City "San Francisco" """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    start = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),pool_pre_ping=True)
    Base.metadata.create_all(start)
    Session = sessionmaker(bind=start)
    session = Session()
    ns = State(name='California')
    nc = City(name='San Francisco')
    ns.cities.append(nc)
    session.add(ns)
    session.add(nc)
    session.commit()

#!/usr/bin/python3
""" lists all cities from hbtn_0e_14_usa db """
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    database_url = 'mysql+mysqldb://{}:{}@localhost/{}' \
        .format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url, pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    query_result = (
        session.query(State.name, City.id, City.name)
        .filter(State.id == City.state_id))

    for result in query_result:
        print(result[0] + ": (" + str(result[1]) + ") " + result[2])

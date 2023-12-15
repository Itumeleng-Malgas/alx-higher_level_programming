#!/usr/bin/python3
"""
lists the first State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    database_url = 'mysql+mysqldb://{}:{}@localhost/{}' \
        .format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url, pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

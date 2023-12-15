#!/usr/bin/python3
"""
lists all State objects that contain the letter a
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

    retrieved_state = session.query(State).filter(State.id == 2).first()
    if retrieved_state:
        retrieved_state.name = "New Mexico"
        session.commit()

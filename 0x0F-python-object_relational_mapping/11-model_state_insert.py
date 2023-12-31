#!/usr/bin/python3
"""
Add new State
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)

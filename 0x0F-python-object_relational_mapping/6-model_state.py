#!/usr/bin/python3
"""Start link class to table in database 
"""
from sqlalchemy import (create_engine)
from model_state import Base, State
import sys

if __name__ == "__main__":
    database_url = 'mysql+mysqldb://{}:{}@127.0.0.1/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
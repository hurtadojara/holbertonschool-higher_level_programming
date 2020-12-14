#!/usr/bin/python3
""" adds to the state object"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    DB_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, DB_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    Louisiana = State(name="Louisiana")
    session.add(Louisiana)
    session.commit()
    print(Louisiana.id)

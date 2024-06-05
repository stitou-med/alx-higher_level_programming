#!/usr/bin/python3
"""deletes states containing letter a"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).filter(State.name.like('%a%')).all()

    for row in rows:
        if "a" in row.name:
            session.delete(row)
    session.commit()

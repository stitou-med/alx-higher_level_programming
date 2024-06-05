#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id).first()

    if not rows:
        print("Nothing")
    else:
        print("{}: {}".format(rows.id, rows.name))

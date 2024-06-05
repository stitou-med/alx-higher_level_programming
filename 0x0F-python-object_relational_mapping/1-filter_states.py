#!/usr/bin/python3
"""
Lists all states with name starting with N from database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE CONVERT(`name` USING Latin1) \
            COLLATE Latin1_General_CS \
            LIKE 'N%';")
    rows = cur.fetchall()

    for row in rows:
        print(row)

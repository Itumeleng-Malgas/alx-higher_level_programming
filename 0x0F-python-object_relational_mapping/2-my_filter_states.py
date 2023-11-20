#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa db where name matches the argv"""

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY
    '{}'".format(sys.argv[4])
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

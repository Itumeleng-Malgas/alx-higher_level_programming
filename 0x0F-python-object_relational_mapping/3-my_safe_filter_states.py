#!/usr/bin/python3
"""Lists all states, Use parameterized query to prevent SQL injection"""

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    name_param = (sys.argv[4],)

    cursor.execute(query, name_param)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

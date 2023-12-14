#!/usr/bin/python3
""" lists all cities from hbtn_0e_4_usadb """
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
    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

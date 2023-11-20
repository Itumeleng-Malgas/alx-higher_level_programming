#!/usr/bin/python3
""" lists all states from hbtn_0e_0_usa db  starting with N """
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
    query = """SELECT * FROM states WHERE name LIKE BINARY 'N%'
    ORDER BY states.id"""
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

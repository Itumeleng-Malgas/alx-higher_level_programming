#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":

    # Get username, password, and database name from command line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    cursor = db.cursor()

    # Execute the query to retrieve states in ascending order by id
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows
    states = cursor.fetchall()

    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()

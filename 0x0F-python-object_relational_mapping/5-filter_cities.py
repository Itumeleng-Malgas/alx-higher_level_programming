#!/usr/bin/python3
"""Lists all cities, Use parameterized query to prevent SQL injection"""

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
    query = """SELECT DISTINCT cities.name FROM cities 
    JOIN states ON states.id=cities.state_id WHERE states.name=%s"""
    name_param = (sys.argv[4],)

    cursor.execute(query, name_param)

    cities = cursor.fetchall()

    # Extract city names from the result and format them
    city_names = [city[0] for city in cities]
    formatted_cities = ', '.join(city_names)

    print(formatted_cities)

    cursor.close()
    db.close()

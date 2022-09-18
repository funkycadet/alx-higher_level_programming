#!/usr/bin/python3
""" Lists matching name values safely in selected table of a database """
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], port=3306)

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id;")
    query_rows = cur.fetchall()

    for state in query_rows:
        print(state)

#!/usr/bin/python3
""" List cities of state passed as an argument from database """
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], port=3306)

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for state in query_rows:
        print(", ".join([state[1] for state in query_rows]))

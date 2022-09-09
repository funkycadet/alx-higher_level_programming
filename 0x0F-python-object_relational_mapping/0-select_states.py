#!/usr/bin/python3
""" 0. Get all states module """
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states;")
    query_rows = cur.fetchall()
    for states in query_rows:
        print(states)

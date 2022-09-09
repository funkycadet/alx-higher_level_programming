#!/usr/bin/python3
""" 2. Filter states by user input module """
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], port=3306)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for state in query_rows:
        print(state)

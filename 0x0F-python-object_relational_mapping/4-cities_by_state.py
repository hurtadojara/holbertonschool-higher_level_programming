#!/usr/bin/python3
'''script that lists cities in db'''

from sys import argv
import MySQLdb


def filter(username, password, db):
    """
    function to list by state
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT\
    JOIN states ON cities.state_id = states.id;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter(argv[1], argv[2], argv[3])

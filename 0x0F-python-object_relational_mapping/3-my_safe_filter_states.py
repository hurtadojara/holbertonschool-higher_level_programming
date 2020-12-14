#!/usr/bin/python3
## secure script againts SQLinjections

from sys import argv
import MySQLdb


def sec_filter(username, password, db, substr):
    """
    a secured filter againts SQL injections
    """
    database = MySQLdb.connect(host="localhost", user=username, passwd=password,
                                db=db, port=3306, charset="utf-8")
    cr = database.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE\
        {}'".format(substr))
    rows = cr.fetchall()
    for row in rows:
        print(row)
    cr.close()
    database.close()

if __name__ == "__main__":
    sec_filter(argv[1], argv[2], argv[3], argv[4])

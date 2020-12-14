#!/usr/bin/python3
# filter states by my substr

from sys import argv
import MySQLdb


def filtro_p(username, password, db, substr):
    """
    filter by the substr
    """
    database = MySQLdb.connect(host="localhost", port=3306, user=username,
                                passwd=password, db=db, charset="utf-8")
    cr = database.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY\
        '{}'".format(substr))
    rows = cr.fetchall()
    for row in rows:
        print(row)
    cr.close()
    database.close()

if __name__ == "__main__":
    filtro_p(argv[1], argv[2], argv[3], argv[4])

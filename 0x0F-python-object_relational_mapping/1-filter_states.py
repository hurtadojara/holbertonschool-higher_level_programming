#!/usr/bin/python3
# filter by starting letter N

from sys import argv
import MySQLdb


def filtro(usern, passw, db):
    """
    filtra por letra N
    """
    database = MySQLdb.connect(host="localhost", port=3306, user=usern,
                                passwd=passw, db=db, charset="utf-8")
    cr = database.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = cr.fetchall()
    for row in rows:
        print(row)
    cr.close()
    database.close()

if __name__ == "__main__":
    filtro(argv[1], argv[2], argv[3])

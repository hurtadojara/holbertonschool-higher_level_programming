#!/usr/bin/python3
'''script that takes the state name and list his cities'''

from sys import argv
import MySQLdb


def filter(usern, password, db, substr):
    """
    function to match a state from db
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=usern,
                         passwd=password, db=db, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                 FROM cities INNER JOIN states ON states.id =\
    cities.state_id WHERE states.name = %s", [substr])
    rows = cur.fetchall()
    cities = ""
    for row in rows:
        cities += str(*row) if cities == "" else ", " + str(*row)
    print(cities)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter(argv[1], argv[2], argv[3], argv[4])

#!/usr/bin/python3
## list states from us states database
from sys import argv
import MySQLdb


def Mbase(username, password, db):
    """
    function to list all states from the database selected
    """
    database = MySQLdb.connect(host="localhost", port=3306, user=username,
                                password=password, db=db)
    cr = database.cursor()
    cr.execute("SELECT * FROM states ORDER BY id ASC")
    q_rows = cr.fetchall()
    for rows in q_rows:
        print(rows)
    cr.close()
    database.close()

if __name__ == "__main__":
    Mbase(argv[1], argv[2], argv[3])

#!/usr/bin/python3
"""
 Displays all values in the states table of the database hbtn_0e_0_usa
 whose name matches that supplied as argument.
 Usage: ./2-my_filter_states.py <mysql username>
                                <mysql password>
                                <database name>
                                <state name searched>
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY \
    id ASC".format(argv[4]))
    states = cursor.fetchall()
    for state in states:
        if state[1] == argv[4]:
            print(state)
    cursor.close()
    db.close()

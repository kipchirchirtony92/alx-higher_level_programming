#!/usr/bin/python3
"""
 script that lists all states from the hbtn_0e_0_usa db
 with a namestarting with N
 Usage: ./1-filter_states.py <mysql username>
                             <mysql password>
                             <database name>

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for state in cursor.fetchall():
        if state[1][0] == 'N':
            print(state)
    cursor.close()
    db.close()

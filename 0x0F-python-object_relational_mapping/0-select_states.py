#!/usr/bin/env python3
# list all the states in the database hbtn_0e_usa
# Usage: ./0-select_states.py <mysql username> \
#                            <mysql password> \
#                            <database name>

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                          port=3306, host="localhost")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")
    for state in cursor.fetchall():
        print(state)

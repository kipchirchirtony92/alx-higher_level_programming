#!/usr/bin/env python3
# Lists all the states with a name starting with N from hbtn_0e_usa db
# usage : ./1-filter_states.py <mysql username>
#                              <mysql password>
#                              <database name>

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    for state in c.fetchall():
        if state[1][0] == "N":
            print(state)

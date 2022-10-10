#!/usr/bin/env python3
"""
  Displays all the values in the state table of the hbtn_0e_0_usa
  whose name matches the supplied argument[4]
  safe from SQL injection
  Usage: .//3-my_safe_filter_states.py <mysql username>
                                       <mysql password>
                                       <mysql name>
                                       <state name searched>

"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306, charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()

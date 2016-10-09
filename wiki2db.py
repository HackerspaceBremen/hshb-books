# -*- coding: utf-8 -*-
import sqlite3
import re

conn = sqlite3.connect('hshb.db')
c = conn.cursor()

id = 1

with open("wiki.txt","r") as f:
    # r = f.readline()
    # print r.split('|')
    # print r.split('|')[1].strip()
    for line in f.readlines():
        values = []
        values.append(id)
        values.append(line.split('|')[1].strip().decode('utf8'))
        values.append(line.split('|')[2].strip().decode('utf8'))
        values.append(line.split('|')[3].strip().decode('utf8'))
        values.append(line.split('|')[4].strip().decode('utf8'))
        # Insert a row of data
        c.execute(u"INSERT INTO Books VALUES (?,?,?,?,?)",values)
        id += 1

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

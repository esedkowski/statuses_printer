import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
con.close()

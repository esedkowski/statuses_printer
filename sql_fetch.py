import sqlite3

database = sqlite3.connect('database.db')
cur = database.cursor()

res = cur.execute('SELECT modelID FROM aircraft WHERE msn="test_msn"')
acID = res.fetchone()
print(acID)

res = cur.execute('SELECT mountID FROM mount WHERE aircraftID=?', acID)
mountID =  res.fetchone()
print(mountID)

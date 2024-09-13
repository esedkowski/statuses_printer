import sqlite3

database = sqlite3.connect('database.db')
cur = database.cursor()

cur.execute('PRAGMA foreign_keys = ON')

cur.execute('CREATE TABLE type (typeID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, desc varchar(255) NOT NULL)')

cur.execute('CREATE TABLE ata (ataID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, typeID FOREGIN KEY REFERENCES type(typeID) NOT NULL, nr varchar(255) NOT NULL, desc varchar(255) NOT NULL)')

cur.execute('CREATE TABLE position (positionID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ataID FOREGIN KEY REFERENCES ata(ataID) NOT NULL, desc varchar(255) NOT NULL)')

cur.execute('CREATE TABLE partNum (partNumID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, partNum varchar(255) NOT NULL, desc varchar(255) NOT NULL)')

cur.execute('CREATE TABLE serialNum (serialNumID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, partNumID FOREGIN KEY REFERENCES partNum(partNumID) NOT NULL, serialNum varchar(255) NOT NULL)')

cur.execute('CREATE TABLE model (modelID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, typeID FOREGIN KEY REFERENCES type(typeID) NOT NULL, desc varchar(255) NOT NULL)')

cur.execute('CREATE TABLE aircraft (aircraftID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, modelID FOREGIN KEY REFERENCES model(modelID) NOT NULL, msn varchar(255) NOT NULL, reg varchar(255) NOT NULL)')

cur.execute('CREATE TABLE mount (mountID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, positionID FOREGIN KEY REFERENCES position(positionID), aircraftID FOREGIN KEY REFERENCES aircraft(aircraftID), serialNumID FOREGIN KEY REFERENCES serialNum(serialNumID))')


cur.execute("""
    INSERT INTO type (desc) VALUES
        ('test_type')
""")

cur.execute("""
    INSERT INTO ata (typeID, nr, desc) VALUES
        (1, '123456789', 'test_ata')
""")

cur.execute("""
    INSERT INTO position (ataID, desc) VALUES
        (1, 'test_position')
""")

cur.execute("""
    INSERT INTO partNum (partNum, desc) VALUES
        (1, 'test_part_num')
""")

cur.execute("""
    INSERT INTO serialNum (partNumID, serialNum) VALUES
        (1, 'test_serial_num')
""")

cur.execute("""
    INSERT INTO model (typeID, desc) VALUES
        (1, 'test_model')
""")

cur.execute("""
    INSERT INTO aircraft (modelID, msn, reg) VALUES
        (1, 'test_msn', 'test_reg')
""")

cur.execute("""
    INSERT INTO mount (positionID, aircraftID, serialNumID) VALUES
        (1, 1, 1)
""")

database.commit()
database.close()

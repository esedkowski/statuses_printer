PRAGMA foreign_keys = ON;

-- setting up database

-- type of aircraft, i.e. B737 NG. Columns: ID, description
CREATE TABLE types (
	typeID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	desc varchar(255) NOT NULL
); 

-- ata. Columns ID, typeID - ATA is specific for type, nr (i.e. 55, 551245), description (i.e. APU, riviet, left wing bottom side middle tab)  
CREATE TABLE ata (
  ataID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	typeID FOREGIN KEY REFERENCES types(typeID) NOT NULL,
	nr varchar(255) NOT NULL,
	desc varchar(255) NOT NULL
); 

-- position, Columns: ID, ataID (one ata can have multiple positions, but position is assigned to one ata, i.e. ATA - Engine, position - LH), description
CREATE TABLE position (
	positionID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	ataID FOREGIN KEY REFERENCES ata(ataID) NOT NULL,
	desc varchar(255) NOT NULL
);

-- part number, one PN can fit many ATAs and positions, Columns: ID, part number, description
CREATE TABLE partNum (
	partNumID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	partNum varchar(255) NOT NULL,
	desc varchar(255) NOT NULL
);

-- serial number, one SN can be assigned to one PN, but there can be many SN assigned to one PN, no need for description, columns: ID, PN ID, SN
CREATE TABLE serialNum (
	serialNumID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	partNumID FOREGIN KEY REFERENCES partNum(partNumID) NOT NULL,
	serialNum varchar(255) NOT NULL
);

-- model, different versions of a type, which share ATA numbers, and most of the components, but might have other differences (i.e. B737-800), columns: ID, type ID, description
CREATE TABLE model (
	modelID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	typeID FOREGIN KEY REFERENCES types(typeID) NOT NULL,
	desc varchar(255) NOT NULL
);

-- aircraft, columns: ID, model ID, MSN (SN for A/C, invidual for each aircraft in type/model, won't change during aircraft operations), registration - individual for each A/C, but can change
CREATE TABLE aircraft (
	aircraftID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	modelID FOREGIN KEY REFERENCES model(modelID) NOT NULL,
	msn varchar(255) NOT NULL,
	reg varchar(255) NOT NULL
);

-- assigment, couldn't come up with better name, connection between position-aircraft or parent component-child component, columns: ID, position ID, parent ID (aircraft or component, should be only one), child ID
CREATE TABLE assigment (
	assigmentID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	positionID FOREGIN KEY REFERENCES position(positionID),
	aircraftID FOREGIN KEY REFERENCES aircraft(aircraftID),
	parentComponentID FOREGIN KEY REFERENCES serialNum(serialNumID),
	serialNumID FOREGIN KEY REFERENCES serialNum(serialNumID)
);

-- documents, columns: ID, path
-- curently unused
CREATE TABLE document (
	documentID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	docPath varchar(255) NOT NULL
);

-- component reference (in document to be replaced by existing data, i.e. LG ENG), columns: ID, name
-- curently unused
CREATE TABLE componentRefrences (
	componentRefrencesID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name varchar(255) NOT NULL
);

-- referenced assigment - to check out latter if necessary
-- CREATE TABLE referencedMount (referencedAssigmentID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, componentRefrencesID FOREGIN KEY REFERENCES componentRefrences(componentRefrencesID), assigmentID FOREGINKEY REFERENCES assigment(assigmentID);

------ test values ------

INSERT INTO types (desc) VALUES ('test_type');

INSERT INTO ata (typeID, nr, desc) VALUES (1, '123456789', 'test_ata');

INSERT INTO position (ataID, desc) VALUES (1, 'test_position');

INSERT INTO partNum (partNum, desc) VALUES (1, 'test_part_num');

INSERT INTO serialNum (partNumID, serialNum) VALUES (1, 'test_serial_num');

INSERT INTO model (typeID, desc) VALUES (1, 'test_model');

INSERT INTO aircraft (modelID, msn, reg) VALUES (1, 'test_msn', 'test_reg');

INSERT INTO assigment (positionID, aircraftID, serialNumID) VALUES (1, 1, 1);

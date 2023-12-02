

import sqlite3

connection = sqlite3.connect('project.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE STATION(
	id INT PRIMARY KEY, 
	name TEXT NOT NULL);
	''')

cursor.execute('''CREATE TABLE ROUTES(
	route_id INT PRIMARY KEY,
	origin INT NOT NULL,
	destination INT NOT NULL,
	FOREIGN KEY (origin) REFERENCES STATION(id),
	FOREIGN KEY (destination) REFERENCES STATION(id));
	''')

cursor.execute('''CREATE TABLE OPERATOR (
	operator_id INT PRIMARY KEY,
	name TEXT NOT NULL,
	address TEXT NOT NULL,
	ph_no TEXT NOT NULL CHECK(LENGTH(ph_no) = 10),
	email TEXT NOT NULL);
	''')

cursor.execute('''CREATE TABLE BUSES(
	id INT PRIMARY KEY,
	type TEXT NOT NULL ,
	capacity INT NOT NULL,
	fare INT NOT NULL,
	op_id INT NOT NULL,
	r_id INT NOT NULL,
	FOREIGN KEY (op_id) REFERENCES OPERATOR(operator_id),
	FOREIGN KEY (r_id) REFERENCES ROUTES(route_id));
	''')

print(cursor.fetchall())

cursor.execute('''CREATE TABLE JOURNEY(
	journey_id INT PRIMARY KEY,
	journey_date TEXT NOT NULL,
	bus_id INT NOT NULL,
	avalable_seats INT NOT NULL,
	FOREIGN KEY (bus_id) REFERENCES BUSES(id));
	''')

cursor.execute('''CREATE TABLE BOOKING(
	journey int NOT NULL,
	name TEXT NOT NULL,
	sex CHAR(1) NOT NULL CHECK(sex IN ('M', 'F')),
	seats INT NOT NULL,
	mob_no TEXT NOT NULL CHECK(LENGTH(mob_no) = 10),
	age INT NOT NULL,
	total_fare INT NOT NULL,
	FOREIGN KEY (journey) REFERENCES JOURNEY(journey_id));
	''')


connection.close()
import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	#obtenemos un cursor de la BD
	c = connection.cursor()

	#Creamos la tabla
	c.execute(""" CREATE TABLE IF NOT EXISTS tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
		status INTEGER NOT NULL)""")

	#Llenamos la BD
	c.execute(
		'INSERT INTO tasks (name, due_date, priority, status)'
		'VALUES("Finish this tutorial","02/03/2014",10,1)'
		)
	c.execute(
	    'INSERT INTO tasks (name, due_date, priority, status)'
	    'VALUES("Finish Real Python Course 2", "02/03/2014", 10, 1)'
	)
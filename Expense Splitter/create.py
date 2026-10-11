import sqlite3

connection= sqlite3.connect('split_database.db')
cursor= connection.cursor()

command_line= """CREATE TABLE simple_table(name VARCHAR(30), expense INT, note TEXT)"""
cursor.execute(command_line)
connection.close()
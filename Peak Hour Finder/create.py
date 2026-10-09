import sqlite3
connection=  sqlite3.connect("the_database.db")

cursor= connection.cursor()
cursor.execute("""CREATE TABLE data_table(time INT, mode INT)""")

connection.close()
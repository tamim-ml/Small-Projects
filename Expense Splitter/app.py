import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import sqlite3
app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	connection= sqlite3.connect('split_database.db')
	cursor= connection.cursor()
	if request.method=='POST':
		name= request.form.get('names')
		expense= request.form.get('expenses')
		note= request.form.get('notes')
		if name != None:
			name= name.lower()
		if expense != None:
			expense= int(expense)
		cursor.execute("INSERT INTO simple_table(name, expense, note) VALUES (?,?,?)",(name,expense,note))
		confirm= request.form.get('confirm')
		if confirm=="remove":
			cursor.execute("DELETE FROM simple_table")
		connection.commit()
		connection.close()
		return render_template('index.html')


	return render_template('index.html')
@app.route("/result")
def result():
	conn=sqlite3.connect('split_database.db')
	data="SELECT name,expense FROM simple_table"
	df= pd.read_sql_query(data, conn, index_col=None )
	df_group= df.groupby('name')['expense'].sum()
	df_group2=df_group
	print(df_group)
	print(df_group.sum())
	print(len(df))
	if df_group.sum()<=0 or len(df_group)<=0:
		average_expense=0
	else:
		average_expense= float(df_group.sum()/len(df_group))
	df_group2=df_group2.astype(float)
	for i in df_group2.index:
		df_group2[i]-=average_expense
	print(df_group2)


	return render_template('result.html', df_group2=df_group2, average_expense=average_expense)
if __name__=="__main__":
	app.run(debug=True, port=1200)
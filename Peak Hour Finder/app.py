import pandas as pd
import numpy as np
from flask import Flask, render_template,request
from datetime import datetime
import sqlite3


app= Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
	connection=sqlite3.connect('the_database.db')
	cursor= connection.cursor()
	if request.method=='POST':
		time= request.form.get('times')
		mode=request.form.get('mode')
		time=int(time)
		mode=int(mode)
		cursor.execute("INSERT INTO data_table(time, mode) VALUES (?,?)",(time,mode))
		connection.commit()
		connection.close()
	return render_template('index.html')
@app.route('/insights')
def insights():
	conn= sqlite3.connect('the_database.db')
	query="SELECT * FROM data_table"
	df=pd.read_sql_query(query, conn)
	df_group= df.groupby('time')["mode"].mean()
	df_group_html= df_group.to_frame().to_html()
	print(df_group)
	df_html= df.to_html(classes="The_data")
	df_group_pd= pd.DataFrame(df_group)
	df_group_max_index= df_group_pd["mode"].idxmax()
	df_group_max_values=df_group_pd.max()

	df_group_min_index=df_group_pd["mode"].idxmin()
	df_group_min_values= df_group_pd.values.min()

	
	
	
	print(df_group[10])



	return render_template('insights.html',df_group_html=df_group_html,df_group_max_values=df_group_max_values,df_group_max_index=df_group_max_index, df_group_min_values=df_group_min_values, df_group_min_index=df_group_min_index)



if __name__=="__main__":
	app.run(debug=True)
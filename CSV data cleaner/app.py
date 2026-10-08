import pandas as pd
import numpy as np

class data_cleaner:
  def __init__(self, data_file):
    self.df=data_file
  
  def run(self):
    #Removing Duplicate.
    self.df=self.df.drop_duplicates()
    #Removing all nul row.
    self.df= self.df.dropna() 
    self.df.columns= self.df.columns.str.capitalize()
    self.df.to_csv('cleaned_data.csv', index=False)

file_type= input("Enter file type: CSV or Excel?")
file_path= input("Enter Your file path: > ")
if file_type.lower()=="csv":
	df=pd.read_csv(file_path)
	cleaned_data= data_cleaner(df)
	cleaned_data.run()
elif file_type.lower()=="excel":
	df=df.pd.read_excel(file_path)
	cleaned_data= data_cleaner(df)
	cleaned_data.run()
else:
	print("Please Enter correct file...")


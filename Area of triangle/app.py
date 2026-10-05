from flask import Flask, render_template,request
import math

app= Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method=='POST':
		a= request.form.get('a')
		b= request.form.get('b')
		c= request.form.get('c')
		a=int(a)
		b=int(b)
		c= int(c)
		s=(a+b+c)/2
		if s>0:
			area = math.sqrt(s*(s-a)*(s-b)*(s-c))
			area=round(area)
		else:
			area= 0
		title="Area of triangle is:"
		return render_template('index.html', areas= area, title= title)
	return render_template('index.html')

if __name__=="__main__":
	app.run(debug=True)
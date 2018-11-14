from flask import Flask,render_template,request
from data1 import Employees
app=Flask(__name__)

getEmp=Employees()

@app.route('/Employee')
def emp():
    return render_template('Emplist.html',myemp=getEmp)

@app.route('/')
def send():
    return render_template('home1.html')



if(__name__=='__main__'):
    app.run(debug=True)

     
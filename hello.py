from flask import Flask, request
from flask import render_template
import json


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
@app.route('/hello.html',methods=['GET', 'POST'])
def hello():

    var="here is a variable"
    var_list=[ 1,2,3 ]    
    var_dict={ "listname" : "hello" }  

    return render_template("alex.html", var=var, var_list=var_list, var_dict=var_dict)


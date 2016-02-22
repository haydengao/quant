#encoding:utf-8
from flask import (Flask, render_template, request, jsonify)

app = Flask(__name__)

@app.route('/')
def strategy():
    listt = [{'a':'1','b':'2','c':'3'},{'a':'4','b':'5','c':'6'}]
    a = 'apple'
    return render_template('test.html',a)

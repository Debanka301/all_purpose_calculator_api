from flask import Flask,jsonify
import math

app = Flask(__name__)

@app.route("/")
def hello_world():
    instructions={
        "API Name":"Calculator for everything API",
        "A guide/Manual":"How to Use this API",
        "For Addition":"Type this:- url/add/num1/num2",
        "For Division":"Type this:- url/divide/num1/num2",
        "For Multiplication":"Type this:- url/multiply/num1/num2",
        "For Subtraction":"Type this:- url/subtract/num1/num2",
        "For Log to the base 10":"Type this:- url/lb10/num1",
        "For Log to the base 2":"Type this:- url/lb2/num1",
        "For Squaring":"Type this:- url/square/num1"
    }
    return jsonify(instructions)
    # return "<p>Hello, World!</p>"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    addd= a+b
    result={
        "Number a":a,
        "Number b":b,
        "Result of Addition":addd
    }
    return jsonify(result)

@app.route("/divide/<int:a>/<int:b>")
def divide(a,b):
    divi= a/b
    result={
        "Number a":a,
        "Number b":b,
        "Result of Division":divi
    }
    return jsonify(result)

@app.route("/multiply/<int:a>/<int:b>")
def multiply(a,b):
    mul= a*b
    result={
        "Number a":a,
        "Number b":b,
        "Result of Multiplication":mul
    }
    return jsonify(result)

@app.route("/subtract/<int:a>/<int:b>")
def subtract(a,b):
    sub= a-b
    result={
        "Number a":a,
        "Number b":b,
        "Result of Addition":sub
    }
    return jsonify(result)

@app.route("/lb10/<int:a>")
def lb10(a):
    res= math.log10(a)
    result={
        "Number a":a,
        "Result of Log to the base 10":res
    }
    return jsonify(result)

@app.route("/lb2/<int:a>")
def lb2(a):
    res= math.log2(a)
    result={
        "Number a":a,
        "Result of Log to the base 2":res
    }
    return jsonify(result)

@app.route("/square/<int:a>")
def square(a):
    res= math.pow(a,2)
    result={
        "Number a":a,
        "Result of square":res
    }
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)
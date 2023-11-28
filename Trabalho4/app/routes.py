from app import app
from flask import jsonify, request
from functions import *

#Root
@app.route('/index')
@app.route('/')
def index():
    return "<h1>MY API</h1>"

#API
@app.route('/my-api', methods=['POST'])
def my_api():

    data = request.get_json()
    errorHandle(data)

    for key, value in data.items():
        if key == 'fact':
            data[key] = factorial(value)
        elif key == 'fib':
            data[key] = fib(value)

    return jsonify(data)

from flask import Flask, render_template, jsonify
from random import *
from todo_registry import *


# @app.route('/')
# def index():
#     return render_template("index.html")


# fixed route to catch the path.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


app.run(host='127.0.0.1', port=8000, debug=True)
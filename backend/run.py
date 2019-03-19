# -*- coding: utf-8 -*-

from todo_app import app, api
from flask import render_template

from todo_app.apis import *


# fixed route to catch the path.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


app.run(host='127.0.0.1', port=9200, debug=True)

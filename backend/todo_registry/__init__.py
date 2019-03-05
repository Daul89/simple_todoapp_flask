# -*- coding: utf-8 -*-
from io import open
import markdown
import os
from flask import Flask, g, jsonify
import shelve
from flask_restful import Resource, Api, reqparse


# create instance
### Todo : app object to be generated in top-level directory. such a messy rel-path
### blocked : cannot share the global app object with current_app. f***

# app = Flask(__name__)
app = Flask(__name__,
            static_folder = "../../dist/static",
            template_folder = "../../dist")
api = Api(app)


# DB connection
### Todo : Change to use DB(sqalchemy) instead of using shelve
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("tasks.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/help')
def index():
    """Index -> present README.md"""

    # open the README file
    with open(os.path.dirname(app.root_path) + '/README.md',
              'r', encoding="utf-8") as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # convert to html
        return markdown.markdown(content)


# endpoint /tasks
class ListTasks(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        tasks = []

        for key in keys:
            tasks.append(shelf[key])

        return {'message': 'Success', 'data': tasks}, 200

### todo : ID better to be auto-incremented + todo item needs to have boolean:done field
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id', required=True)
        parser.add_argument('item', required=True)

        args = parser.parse_args()

        shelf = get_db()
        shelf[args['id']] = args

        return {'message': 'Task Created', 'data': args}, 201


api.add_resource(ListTasks, '/tasks')


# endpoint /task
class Task(Resource):

    def get(self, id):
        shelf = get_db()
        if not (id in shelf):
            return {'message': 'ID Not Found', 'data': {}}, 404

        return {'message': 'Success', 'data': shelf[id]}, 200

    def delete(self, id):
        shelf = get_db()
        if not (id in shelf):
            return {'message': 'ID Not Found', 'data': {}}, 404

        del shelf[id]
        return '', 204


api.add_resource(Task, '/task/<string:id>')

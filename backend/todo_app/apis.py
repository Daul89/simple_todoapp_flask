# -*- coding: utf-8 -*-
from io import open
import markdown
import os
from flask import Flask, g, jsonify, request
from flask_restful import Resource, Api, reqparse
from todo_app import app, api
from database import db
from .models import Todos, todo_schema, todos_schema
from .utils import __EmptyDictError, __is_empty_dict
from sqlalchemy.exc import SQLAlchemyError

"""
Todo :  SQL Injection
        DB Migrate
        Module to Generate sample data
        Source code trimming
        Blue Print
"""

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
class TodoList(Resource):

    def get(self):      
        try:
            all_todos = Todos.query.all()
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error_msg": str(e)}, 403
        return todos_schema.jsonify(all_todos)

    # validation check in models
    def post(self):
        try:
            todo_dict = request.get_json(force=True)
            new_todo = Todos(todo_dict['item'])
            new_todo.add(new_todo)
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error_msg": str(e)}, 403
            
        return todo_schema.jsonify(new_todo)

"""
Todo : empty dict error handling
"""
class Todo(Resource):
   
    def get(self, id): 
        # if not valid id, response 404
        try:
            #todo = Todos.query.get_or_404(id)
            todo = Todos.query.get_or_404(id)
#            __is_empty_dict(todo)
#        except __EmptyDictError:
#            return {"error_msg": "id not existing"}, 404

        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error_msg": str(e)}, 403

        return todo_schema.jsonify(todo)

    def delete(self, id):
        # if not valid id, response 404
        try:
            todo = Todos.query.get_or_404(id)
#            __is_empty_dict(todo)
            todo.delete(todo)
        except AttributeError:
            return {"error_msg": "id not existing"}, 404
#        except __EmptyDictError:
#            return {"error_msg": "id not existing"}, 404
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error_msg": str(e)}, 403

        return {"message": "Deleted"}, 204

    def put(self, id):
        # if not valid id, response 404
        todo = Todos.query.get_or_404(id)
        todo_dict = request.get_json(force=True)
        print (todo_dict)
        try:
            todo_schema.validate(todo_dict)
            for key, value in todo_dict.items():
                
                setattr(todo, key, value)
          
            todo.update()            
            return self.get(id)

        except AttributeError:
            return {"error_msg": "id not existing"}, 404
#        except __EmptyDictError:
#            return {"error_msg": "id not existing"}, 404
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error_msg": str(e)}, 403

        return todo_schema.jsonify(todo)

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<int:id>')


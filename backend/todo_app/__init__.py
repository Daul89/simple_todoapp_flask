# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_cors import CORS


# create instance
#app = Flask(__name__)
app = Flask(__name__,
            static_folder = "../../dist/static",
            template_folder = "../../dist")

api = Api(app)

cors = CORS(app, resources={
  r"/*": {"origin": "*"},
})


import todo_app.apis
import todo_app.models
import database

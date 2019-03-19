from database import db, CRUD
from todo_app import app
from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy.orm import validates

# Init ma
ma = Marshmallow(app)


### todo item needs to have boolean:done field
# model definition
class Todos(db.Model, CRUD):
    __tablename__ = 'todos'
    id = db.Column('id', db.Integer, primary_key=True)
    item = db.Column('item', db.String(50))

    def __repr__(self):
        return '<Todos id={id} item={item!r}>'.format(
                id=self.id, item=self.item)

    def __init__(self, item):
        self.item = item

    # validation for item
    @validates('item')
    def validate_item(self, key, item):
        if not item:
            raise AssertionError('No item provided')
        if len(item) < 1:
            raise AssertionError('Todo item must NOT be blank')
        if len(item) > 50:
            raise AssertionError('Todo item must NOT be greater than 50')

        return item


# Schema by Marshmallow for json serialization purpose.
class TodosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'item')


# Init Schema
todo_schema = TodosSchema(strict=True)
todos_schema = TodosSchema(many=True, strict=True)


# def init():
#     db.create_all()

# init()
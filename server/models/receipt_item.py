from flask import Flask
from mongoengine import Document, StringField, IntField, FloatField
app = Flask(__name__)

class recept_item(Document):
    name = StringField()
    id = IntField(primary_key=True)
    price= FloatField()

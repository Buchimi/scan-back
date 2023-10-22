# from dataclasses import dataclass
from flask import Flask
from mongoengine import Document, StringField, IntField, FloatField
app = Flask(__name__)

# @dataclass
class recept_item(Document):
    name = StringField()
    id = IntField(primary_key=True)
    price= FloatField()
    
# pydantic json into class
# benie 
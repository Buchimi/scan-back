from mongoengine import Document, StringField, FloatField

class User(Document):
    username: StringField
    savings: FloatField
    
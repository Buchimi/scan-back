from mongoengine import Document, StringField, IntField, FloatField

class reciept_item(Document):
    
    name = StringField()
    price= FloatField()

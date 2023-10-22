from mongoengine import Document, StringField, IntField, FloatField

class reciept_item(Document):
    id = IntField(primary_key=True)
    name = StringField()
    price= FloatField()

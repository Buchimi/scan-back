from mongoengine import Document, StringField, IntField, FloatField

class recept_item(Document):
    id = IntField(primary_key=True)
    name = StringField()
    price= FloatField()

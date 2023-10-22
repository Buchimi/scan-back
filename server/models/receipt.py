import datetime
from mongoengine import Document, ListField, DateField, IntField, StringField

class Receipt(Document):
    items = ListField()
    when = DateField(default=datetime.datetime.utcnow)
    id = IntField(primary_key=True)
    owner = StringField()

    

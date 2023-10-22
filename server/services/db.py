from configs.setup import connect_db
from models import receipt_item, user
import mongoengine 

class Client():
    def __init__(self):
        self.client = connect_db()

    def save_receipt_item_to_db():
        item = receipt_item(id = 0, name = 'Name of the product', price = 10)

        # this writes it to the database
        item.save()
        pass
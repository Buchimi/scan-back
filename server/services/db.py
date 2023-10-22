from configs.setup import connect_db

class Client():
    def __init__(self):
        self.client = connect_db()
from flask import Flask
from controllers.upload_image import upload_image_bp
from services.db import Client
from services.scraper import Scraper
from controllers.receipt import reciept_bp
from controllers.receipt_item import receipt_item_bp
from controllers.user import user_bp

app = Flask(__name__)
app.register_blueprint(upload_image_bp)
app.register_blueprint(reciept_bp)
app.register_blueprint(receipt_item_bp)
app.register_blueprint(user_bp)

# make database connection
db = Client()

# create the scraper
scraper = Scraper()
# scraper.scrape_item_price(name="KNDR BLEND")

if __name__ == '__main__':
    app.run()
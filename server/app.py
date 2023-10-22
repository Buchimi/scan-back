from flask import Flask
from controllers.upload_image import upload_image_bp
from services.db import Client
from services.scraper import Scraper

app = Flask(__name__)

# make database connection
db = Client()

# create the scraper
scraper = Scraper()
scraper.scrape_item_price(name="KNDR BLEND", price=4.22)

app.register_blueprint(upload_image_bp)

if __name__ == '__main__':
    app.run()
from flask import Flask
from routes.upload_image import upload_image
from services.db import Client
from services.scraper import Scraper

app = Flask(__name__)

# make database connection
db = Client()

# create the scraper
scraper = Scraper()

# app.register_blueprint(upload_image_bp)

if __name__ == '__main__':
    app.run()
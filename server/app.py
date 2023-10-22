# from flask_migrate import Migrate
# from routes.blueprint import blueprint
from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("USER_MONGODB")
password = os.getenv("PASS_MONGODB")
mongo_uri = uri = f"mongodb+srv://{username}:{password}@scan-back-cluster.eoldn4r.mongodb.net/?retryWrites=true&w=majority"

def create_app():
    app = Flask(__name__) 
    # app.config.from_object('config')  # Configuring from Python Files
    return app

app = create_app()
client = MongoClient(uri, server_api=ServerApi('1'))

@app.route('/upload_image', methods=['POST'])
def upload_image():
    data = request.get_json()
    base64_image = data.get('image_data')

    # process the photo
    # do business logic with the photo (machine learning part)
    # and database database things

    # list of savings that can be applied to receipt
    savings = {"This is a dictionary that contains the savnigs": "These are the savings that a user will have"}
    return jsonify(savings)

# app.register_blueprint(blueprint)
# migrate = Migrate(app, db)  # Initializing the migration

if __name__ == '__main__':
    app.run()
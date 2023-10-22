from flask import Blueprint, request, jsonify
from services.ml_model import ML_model
from models import receipt_item

upload_image_bp = Blueprint('upload_image', __name__)

@upload_image_bp.route('/uplaod_image', methods=['POST'])
def upload_image():
    data = request.get_json()
    base64_image = data.get('image_data')

    model = ML_model()
    receipt_items = model.get_receipt_items(base64_image)

    for item in receipt_items:
        print(item)

    # do business logic with the photo (machine learning part)
    # and database database things

    # list of savings that can be applied to receipt
    savings = {"This is a dictionary that contains the savnigs": "These are the savings that a user will have"}
    return jsonify(savings)

from flask import Blueprint, request, jsonify

upload_image_bp = Blueprint('upload_image', __name__)

@upload_image_bp.route('/uplaod_image', methods=['POST'])
def upload_image():
    data = request.get_json()
    base64_image = data.get('image_data')

    # process the photo
    # do business logic with the photo (machine learning part)
    # and database database things

    # list of savings that can be applied to receipt
    savings = {"This is a dictionary that contains the savnigs": "These are the savings that a user will have"}
    return jsonify(savings)

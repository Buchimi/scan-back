from flask import Blueprint, request
from models.receipt_item import reciept_item

receipt_item_bp = Blueprint("receipt_item", __name__)

@receipt_item_bp.route("/reciept_item/<id>", methods=["POST"])
def create_receipt_item(id):
    data = request.get_json()
    rec_item = reciept_item.from_json(data)
    rec_item.id = id
    rec_item.save()
    return rec_item.to_json()

@receipt_item_bp.route("/reciept_item/<id>", methods=["GET"])
def get_receipt_item(id):
    return reciept_item.objects(id=id).to_json()

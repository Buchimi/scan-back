from flask import Blueprint, request
from models.receipt_item import reciept_item
from typing import List

receipt_item_bp = Blueprint("receipt_item", __name__)

@receipt_item_bp.route("/reciept_item/<id>", methods=["POST"])
def create_receipt_item(id):
    data = request.get_json()
    rec_item = reciept_item.from_json(data)
    
    rec_item.save()
    return rec_item.to_json()

@receipt_item_bp.route("/reciept_item/<id>", methods=["GET"])
def get_receipt_item(id):
    return reciept_item.objects(id=id).to_json()


@receipt_item_bp.route("/reciept_item/list", methods=["POST"])
def accept_receipt_list():
    data: List = request.get_json()

    for item in data:
        val = reciept_item.from_json(item)
        val.save()
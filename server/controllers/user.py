from flask import Blueprint, request
from models.user import User
user_bp = Blueprint('user', __name__)

@user_bp.route("/user/<id>", methods=["PUT"])
def updateUser(id):
    data = request.get_json()
    user = User.from_json(data)
    user.id = id
    user.save()
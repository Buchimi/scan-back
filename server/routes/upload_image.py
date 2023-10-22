from flask import Blueprint
from controllers.machineController import index, create, insert

blueprint = Blueprint('blueprint', __name__)
blueprint.route('uplaod_photo', methods=['POST'])(upload_photo)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['GET'])(insert)
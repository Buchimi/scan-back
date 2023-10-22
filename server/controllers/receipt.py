from flask import Blueprint, request, jsonify

reciept_bp = Blueprint("receipt", __name__)

@reciept_bp.route("/reciept/<id>", methods=["GET"])
def get_receipt(id):
    # use the db connection to get the receipt
    '''
    User model
    Fields
        - id: int
        The id of the user

        - savings: float
        The savings of the user over all time

    There is a need to be able to display the amount of user savings generated through the app
    To do this we need to access the previous receipts of a user and store them in an array

    Receipt_history model
    Fields
        - user_id: int
        - recepits: list[recepts]
        - savings: float (generated field)


    We could also store the actual prices of each product (on walmart website) in it's own 
    table and update said price when we scan.

    Product model
    Fields
        - id: int
        - name: string
        - price: float

    
    
    I'll like the mobile app to have a fake digital store for walmart products.
    product: {
    product_id (serial code),
    product_name,
    price,
    pic_url
    }

    This can be useful for spending savings on our "fake store"

    I expect:
    create, update, get endpoint for User

    get endpoint for product
    get endpoint for receipt
    '''
    pass
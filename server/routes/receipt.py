from flask import Blueprint, request, jsonify

reciept_bp = Blueprint("receipt", __name__)

@reciept_bp.route("/reciept/<id>", methods=["POST"])
def getid():
    '''

    We need the user object 
    {
    id,
    savings
    }

    We need to be able to display user savings generated. 
        To do this we need access to the previous reciepts of a user which stores an array
        of products 
        receipt (or transaction) :{
        receipt_id,
        user_id,
        product[]
        }

        We could also store the actual prices of each product (on walmart website) in it's own 
        table and update said price when we scan.

        
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
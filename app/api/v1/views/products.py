from flask import Flask, Blueprint, jsonify, request
from app.api.v1.models.products_model import Product
from app.api.v1.models.store_model import Store
products = Blueprint('products', __name__)


@products.route('/')
def welcome():
    return "This is the store manager application"


@products.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(Store.get_all_products())


@products.route('/products/<productId>', methods=['GET'])
def get_specific_product(productId):
    response = Store.get_specific_product(productId)
    print("RESPONSE ", response)
    if(response):
        return jsonify(response), 200
    return jsonify({"message": "a product with that ID was not found"}), 200


# @products.route('/products')


#  Method to create a new product in the store and to update products in stock
@products.route('/products', methods=['POST', 'PUT'])
def post_product():
    product_to_update = request.args.get('id')
    quantity_to_adjust = request.args.get('qty')
    if product_to_update and quantity_to_adjust:
        Store.update_product(product_to_update, quantity_to_adjust)
        return "success", 204
    else:
        # append_new_product_to_store()
        #  reading the request
        req_data = request.get_json()
        product_id = "P" + str(len(Store.products) + 1)
        name = req_data['name']
        curr_qty = req_data['curr_qty']
        min_qty = req_data['min_qty']
        price = req_data['price']
        category = req_data['category']

        #  creating product object
        product = Product(product_id, name, curr_qty, min_qty, price, category)
        response = product.post_product()
        if response == 'success':
            return 'success : product successfully appended to records', 201
        else:
            return 'fail : the sale transaction did not go through', 400

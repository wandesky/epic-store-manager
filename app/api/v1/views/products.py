from flask import Flask, Blueprint, jsonify, request
from app.api.v1.models.products_model import Product
from app.api.v1.models.store_model import Store
products = Blueprint('products', __name__)

@products.route('/')
def welcome():
    return "This is the store manager application"

@products.route('/products', methods = ['GET'])
def get_all_products():
    # store = Store()
    return jsonify(Store.get_all_products())

@products.route('/products', methods = ['POST'])
def post_product():
    
    #reading the request
    req_data = request.get_json()
    product_id = "P" + str(len(Store.products) + 1)
    name = req_data['name']
    curr_qty = req_data['curr_qty']
    min_qty = req_data['min_qty']
    price = req_data['price']
    category = req_data['category']

    #creating product object
    product = Product(product_id, name, curr_qty, min_qty, price, category)
    response = product.post_product()
    if response == 'success':
        return 'success : product successfully appended to records', 201
    else:
        return 'fail : the sale transaction did not go through, possible invalid request', 400
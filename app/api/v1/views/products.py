from flask import Flask, Blueprint, jsonify, request
# from app.api.v1.models.products import Product
from app.api.v1.models.store_model import Store
products = Blueprint('products', __name__)

@products.route('/')
def welcome():
    return "This is the store manager application"

@products.route('/products', methods = ['GET'])
def get_all_products():
    store = Store()
    print('All products: ', jsonify(store.get_all_products()))
    return jsonify(store.get_all_products())
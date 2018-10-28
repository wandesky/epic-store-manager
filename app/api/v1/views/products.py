from flask import Flask, Blueprint, jsonify
from app.api.v1.models.products import products_model
products = Blueprint('products', __name__)

@products.route('/')
def hello():
    return "This is the hello world application"

@products.route('/sales')
def get_all_sales():
    return jsonify(sales_model)
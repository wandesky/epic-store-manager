from flask import Flask, Blueprint, jsonify
from app.api.v1.models.sales import sales_model
sales = Blueprint('sales', __name__)

@sales.route('/')
def hello():
    return "This is the hello world application"

@sales.route('/sales')
def get_all_sales():
    return jsonify(sales_model)
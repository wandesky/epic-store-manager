from flask import Flask, Blueprint, jsonify
# from app.api.v1.models.sales_model import Sale
from app.api.v1.models.store_model import Store
sales = Blueprint('sales', __name__)

@sales.route('/')
def hello():
    return "This is the hello world application"

@sales.route('/sales')
def get_all_sales():
    store = Store()
    print('All sales: ', jsonify(store.get_all_sales()))
    return jsonify(store.get_all_products())
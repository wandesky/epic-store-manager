from flask import Flask, Blueprint, jsonify, request
from app.api.v1.models.sales_model import Sale
from app.api.v1.models.store_model import Store
sales = Blueprint('sales', __name__)

@sales.route('/')
def hello():
    return "This is the hello world application"

@sales.route('/sales', methods = ['GET'])
def get_all_sales():
    all_sales = Store.get_all_sales()
    if all_sales:
        return jsonify(all_sales)
    else:
        return "The sale records are empty"

@sales.route('/sales', methods = ['POST'])
def post_sale():
    
    #reading the request
    req_data = request.get_json()
    sale_id = req_data['sale_id']
    product_id = req_data['product_id']
    quantity_sold = req_data['quantity_sold']
    amount = req_data['amount']

    #creating sale object
    sale = Sale(sale_id, product_id, quantity_sold, amount)
    # store = Store()
    response = sale.post_sale()
    if response == 'success':
        return 'sale transaction successfully processed', 201
    else:
        return 'the sale transaction did not go through, possible invalid request', 400
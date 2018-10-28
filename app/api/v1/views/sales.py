from flask import Flask, Blueprint
sales = Blueprint('profile', __name__)

@sales.route('/hello')
def mambo():
    return 'poa'
# import app

# sales_app = app.create_app()

# @sales_app.route('/hello')
# def baseUrl():
#     return 'Base, URL'

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello"
from flask import Flask, Blueprint
from app.api.v1.views.sales import sales


app = Flask(__name__)
app.register_blueprint(sales)
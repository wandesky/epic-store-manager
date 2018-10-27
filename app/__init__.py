from flask import Flask, Blueprint
from instance.config import app_config
# from app.api.v1.views.products import Products
# from app.api.v1.views.sales import Sales

def create_app(config_name):
    app = Flask(__name__)
    # api = Api(app)
    return app
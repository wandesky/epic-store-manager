from flask import Flask, Blueprint, jsonify
errors = Blueprint('errors', __name__)

@errors.route('/')
def hello():
    return "Seems like you've got some routes mixed up here, try writing in the form of /api/v1/products..."
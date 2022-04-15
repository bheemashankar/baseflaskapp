from flask import Flask, jsonify
from apps.api import api_app


@api_app.route('/', strict_slashes=False)
def index():
    data = {"names": 'Flask is running!'}
    return jsonify(data)


@api_app.route('/data', strict_slashes=False)
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

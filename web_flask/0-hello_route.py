#!/usr/bin/python3
"""Modulo to find the flask
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


app.run(debug=True, port=5000)

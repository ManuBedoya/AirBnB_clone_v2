#!/usr/bin/python3
"""Modulo to find the flask
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """The root of the page or index/default
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Page to show the message HBNB
    """
    return 'HBNB'


app.run(debug=True, port=5000)

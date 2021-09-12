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


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Page to show the message C + a word in the url
    """
    separate = text.split("_")
    return 'C {}'.format(' '.join(separate))


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Page to show the message HBNB
    """
    return 'HBNB'


app.run(debug=True, port=5000)

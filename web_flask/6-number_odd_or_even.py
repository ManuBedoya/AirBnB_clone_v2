#!/usr/bin/python3
"""Modulo to find the flask
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """The root of the page or index/default
    """
    return 'Hello HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """Page to show the message C + a word in the url
    """
    separate = text.split("_")
    return 'C {}'.format(' '.join(separate))


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Page to show the message HBNB
    """
    return 'HBNB'


@app.route('/python/<text>', strict_slashes=False)
def python_is(text):
    """Page to show the message Python + a word or phrase in the url
    """
    separate = text.split("_")
    return 'Python {}'.format(' '.join(separate))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Page to show the message number + is a number
    """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Change the h1 tag with the number
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Change the h1 tag with the respecting information id is odd or even
    """
    odd_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html',
                           number=n, odd_even=odd_even)


app.run(debug=True, port=5000)

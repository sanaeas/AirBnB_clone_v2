#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display a hello message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """Display 'C ' followed by the value of the text variable"""
    return f'C {escape(text.replace("_", " "))}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text='is cool'):
    """Display 'Python ' followed by the value of the text variable"""
    return f'Python {escape(text.replace("_", " "))}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display 'n is a number'"""
    return f'{escape(n)} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """Display an HTML page"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

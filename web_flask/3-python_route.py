#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

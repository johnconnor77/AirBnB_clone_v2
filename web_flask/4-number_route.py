#!/usr/bin/python3
"""Script that starts a Flask web app that listens on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """Displays C followed by the value of the text variable"""
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text):
    """Display Python , followed by the value of the text variable"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def show_num(n):
    """Display n is a number only if n is an integer"""
    return '%d is a number' % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
#!/usr/bin/python3


from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer and
    H1 tag: Number: n, inside the tag BODY
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    """Display a HTML page only if n is an integer and
    H1 tag: Number: n is even or odd inside the tag BODY
    """
    number = '{} is even'.format(n) if n % 2 == 0 else '{} is odd'.format(n)
    return render_template('6-number_odd_or_even.html', n=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Returns Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """ Displays “C ”, followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """ Displays Python, followed by the value of the text variable"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def if_num(n):
    """ Displays n, if it's an integer """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def if_num_disp(n):
    """ Displays HTML template, if it's an integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """display a template if even and another if odd"""
    if n % 2 == 0:
        state = "even"
    else:
        state = "odd"
    return render_template('6-number_odd_or_even.html', n=n, state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

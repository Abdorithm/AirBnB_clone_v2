#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def show_states():
    """ Displays all states"""
    states = storage.all(State)

    return render_template('7-states_list.html', states=states.values())


@app.teardown_appcontext
def tear_down(exc):
    """ End the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

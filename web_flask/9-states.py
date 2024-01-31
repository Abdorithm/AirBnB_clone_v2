#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def show_states_and_cities(id=None):
    """ Displays all states"""
    states = storage.all(State)
    if id is not None:
        id = 'State.' + id

    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def tear_down(exc):
    """ End the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

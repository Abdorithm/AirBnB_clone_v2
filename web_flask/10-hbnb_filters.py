#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def HBNB_Filters():
    """ Displays all states"""
    states = storage.all(State)
    amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', states=states.values(),
                           amenities=amenities.values())


@app.teardown_appcontext
def tear_down(exc):
    """ End the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

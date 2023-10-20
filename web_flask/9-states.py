#!/usr/bin/python3
"""
Start a Flask web application
"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """Display a list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def list_state_cities(state_id):
    """Display cities in a state."""
    state = None
    for state_obj in storage.all(State).values():
        if state_obj.id == state_id:
            state = state_obj
            break
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html', state=None, cities=None)


@app.teardown_appcontext
def teardown_session(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

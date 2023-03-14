#!/usr/bin/python3
"""a script that starts a flask application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@ app.route('/', strict_slashes=False)
def print_hello():
    """hbnb"""
    return "Hello HBNB!"


if __name__ == '_main_':
    app.debug = 1
    app.run(host='0.0.0.0', port=5000)

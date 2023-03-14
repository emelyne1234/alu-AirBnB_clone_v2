#!/usr/bin/python3
# starts an application
""" a script that starts a flask application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@ app.route('/', strict_slashes = False)
def print_hello():
    """hbnb"""
    return 'Hello HBNB!'


@ app.route('/hbnb', strict_slashes = False)
def print_hi():
    """ printing hbnb"""
    return HBNB


if __name__ == '__main__':
    print_hi('HBNB')
    app.run = (host="0.0.0.0", port=5000, debug=True)

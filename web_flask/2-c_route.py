#!/usr/bin/python3
"""a script that starts a flask application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@ app.route('/')
def print_hello():
    """hbnb"""
    return "Hello HBNB!"


@ app.route('/hbnb')
def display_hbnb():
    """hbnb"""
    return "HBNB!"


@ app.route('/c/<string:name>')
def c_is_fun(name):
    """C is fun"""
    return "C {}".format(name.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3
"""a script that starts a flask application"""


from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@ app.route('/', strict_slashes=False)
def print_hello():
    """Hello bnb"""
    return "Hello HBNB!"


@ app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

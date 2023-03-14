#!/usr/bin/python3
# starts application
"""a script that starts a flask application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@ app.route('/')
def print_hello(name):
    """hbnb"""
    return (f'Hello {name}!')

if __name__ == '__main__':
    """allows the execution"""
    print_hi('HBNB')
    app.run = (port := 5000, host := "0.0.0.0")

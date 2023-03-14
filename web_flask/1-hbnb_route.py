#!/usr/bin/python3
# starts an application
""" a script that starts a flask application """
from flask import Flask

app = Flask(__name__)


@ app.route('/')
def print_hello(name):
    """hbnb"""
    return (f'Hello {name}!')


@ app.route('/hbnb')
def print_hi(name):
    """ printing hbnb"""
    return name


if __name__ == '__main__':
    print_hi('HBNB')
    app.run = (port := 5000, host := "0.0.0.0")

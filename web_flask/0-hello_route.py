#!/usr/bin/python3
"""starts flask web application"""
from flask import Flask

app = Flask(__name__)


@ app.route('/')
def print_hi(name):
    """ printing hbnb"""
    print(f'Hello {name}!')


if __name__ == '__main__':
    print_hi('HBNB')
app.run = (port := 5000, host := "0.0.0.0")

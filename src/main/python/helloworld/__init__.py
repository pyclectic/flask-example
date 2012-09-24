__author__ = 'Michael Gruber'

from flask import Flask

VERSION = '${version}'

application = Flask(__name__)

@application.route('/')
def index():
    return 'Hello world.'

__author__ = 'Michael Gruber'

from flask import Flask

__version__ = '${version}'

application = Flask(__name__)

@application.route('/')
def index():
    return 'Hello world.'

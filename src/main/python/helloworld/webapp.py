#   flask-hello-world
#   Copyright 2012 Michael Gruber, Alexander Metzner
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


"""
    This module provides a flask application responding with a
    "Hello world"-page when requesting "/".
"""

__author__ = 'Michael Gruber'

from flask import Flask, render_template

from helloworld.services import HelloService


application = Flask(__name__)
hello_service = HelloService()


@application.route('/')
def index():

    return render_template('index.html', title=hello_service.get_title())
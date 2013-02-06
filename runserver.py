#!/usr/bin/env python
#
#   This script will start the hello world application in debug mode.
#
#   author: Michael Gruber

from sys import path
path.append("src/main/python")

from helloworld.webapp import application
application.run(debug=True)

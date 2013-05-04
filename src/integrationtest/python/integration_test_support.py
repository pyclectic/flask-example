#   flask-hello-world
#   Copyright 2012-2013 Michael Gruber, Alexander Metzner
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
    This module provides a IntegrationTestServerFixture which runs a
    IntegrationTestServer on "http://127.0.0.1:5000/".
"""

from multiprocessing import Process
from pyfix import Fixture
from time import sleep
from urllib import urlopen

from helloworld.webapp import application


class IntegrationTestServer(object):

    def __init__(self):
        self._process = Process(target=application.run)
        self._process.start()
        sleep(0.2)

    def stop(self):
        self._process.terminate()

    def get_page(self, url):
        return urlopen('http://127.0.0.1:5000' + url).read()


class IntegrationTestServerFixture(Fixture):

    def reclaim(self, integration_test_server):
        integration_test_server.stop()

    def provide(self):
        return [IntegrationTestServer()]

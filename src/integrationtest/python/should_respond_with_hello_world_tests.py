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
    A integration test which runs the flask application and asserts that
    it sends "Hello world" when requesting "http://127.0.0.1:5000/".
"""

__author__ = 'Michael Gruber, Alexander Metzner'

from multiprocessing import Process
from pyassert import assert_that
from pyfix import test, given, run_tests, Fixture
from time import sleep
from urllib import urlopen

from helloworld.webapp import application

class IntegrationTestServerFixture(Fixture):
    def reclaim(self, process):
        process.terminate()

    def provide(self):
        process = Process(target=application.run)
        process.start()
        sleep(0.2)

        return [process]


@test
@given(integration_test_server=IntegrationTestServerFixture)
def should_send_message_when_requesting_index_page(integration_test_server):
    actual_page_content = urlopen('http://127.0.0.1:5000/').read()
    assert_that(actual_page_content).is_equal_to('Hello world.')

if __name__ == '__main__':
    run_tests()

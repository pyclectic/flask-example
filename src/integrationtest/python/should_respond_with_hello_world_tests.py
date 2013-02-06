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
    it responds with the "Hello world"-page when
    requesting "http://127.0.0.1:5000/".
"""

__author__ = 'Michael Gruber, Alexander Metzner'


from pyassert import assert_that
from pyfix import given, test, run_tests

from integration_test_support import IntegrationTestServerFixture


@test
@given(server=IntegrationTestServerFixture)
def index_page_should_show_title(server):

    actual_page_content = server.get_page('/')
    assert_that(actual_page_content).contains('<h1>Hello, world!</h1>')


if __name__ == '__main__':
    run_tests()

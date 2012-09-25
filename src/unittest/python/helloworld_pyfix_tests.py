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
    Unittest which asserts that the index function returns "Hello world."

    There is another test which prevents you from making the mistake of
    testing the locally installed version instead of the modified source.
    
    If the application has been installed the __version__ string will be
    something like '1.2.3' instead of '${version}'.
"""

__author__ = 'Michael Gruber, Alexander Metzner'

from pyfix import test
from pyassert import assert_that

from helloworld import __version__, index


@test
def should_return_hello_world():
    actual_result = index()

    assert_that(actual_result).is_equal_to('Hello world.')

@test
def if_this_test_fails_maybe_helloworld_has_been_installed_locally():
    assert_that(__version__).is_equal_to('${version}')

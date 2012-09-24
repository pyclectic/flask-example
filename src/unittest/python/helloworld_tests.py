from unittest import TestCase
from pyassert import assert_that

from helloworld import VERSION, index


class HelloWorldTests (TestCase):
    def test_if_this_test_fails_maybe_helloworld_has_been_installed_locally (self):
        assert_that(VERSION).is_equal_to('${version}')


    def test_should_return_hello_world (self):
        actual_result = index()
        
        assert_that(actual_result).is_equal_to('Hello world.')

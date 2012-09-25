from pyfix import test
from pyassert import assert_that

from helloworld import __version__, index

@test
def if_this_test_fails_maybe_helloworld_has_been_installed_locally():
    assert_that(__version__).is_equal_to('${version}')

@test
def should_return_hello_world():
    actual_result = index()

    assert_that(actual_result).is_equal_to('Hello world.')

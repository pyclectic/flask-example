from multiprocessing import Process
from time import sleep
from pyfix import test, given, run_tests, Fixture
from urllib import urlopen
from pyassert import assert_that

from helloworld import application

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

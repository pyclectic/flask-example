from multiprocessing import Process 
from time import sleep
from unittest import TestCase, main
from urllib import urlopen

from helloworld import application

class Test (TestCase):
    def setUp(self):
        self._process = Process(target=application.run)
        self._process.start()
        sleep(0.2)
        
        
    def tearDown(self):
        self._process.terminate()
        
        
    def test (self):
        actual_page_content = urlopen('http://127.0.0.1:5000/').read()
        
        self.assertEqual('Hello world.', actual_page_content)


if __name__ == '__main__':
    main()

import blogapp
import unittest
import os

class TestHandler(unittest.TestCase):
    '''
    a handler class for all other unit tests
    '''
    def setUp(self):
        blogapp.app.config['TESTING'] = True
        self.app = blogapp.app.test_client()
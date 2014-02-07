import blogapp
from main_test_handler import TestHandler

class FrontPageTests(TestHandler):
    '''
    test class for the main page of the app '/'
    '''

    def test_main_app_route(self):
        '''
        test that the main app route returns a 200 response
        '''
        response = self.app.get('/')
        self.assertIn('200', response.status)

import blogapp
from main_test_handler import TestHandler

class BlogPostGetRequestTest(TestHandler):
    '''
    test class for request in the form '/blog/<year>/<month>/<day>'
    '''

    def test_known_blog_get_request(self):
        '''
        test that a get request to the known blog post returns a good response
        '''
        response = self.app.get('/blog/2013/march/27')
        self.assertIn('200', response.status)

    def test_bad_blog_get_request(self):
        '''
        test that a get request for a non-existant blog post returns a 404 msg
        '''
        response = self.app.get('/blog/2303/march/27')
        self.assertIn('404', response.status)

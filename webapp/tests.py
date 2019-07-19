import sys
sys.path.append(".")
import unittest

from pyramid import testing


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        from views.dashboard import my_view

        request = testing.DummyRequest()
        response = my_view(request)
        self.assertEqual(response, {})

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import get_app
        app = get_app('../development.ini')
        from webtest import TestApp

        self.testapp = TestApp(app)


    def test_dv(self):
        res = self.testapp.get('/view/1', status=200)
        self.assertEqual(res.content_type, 'text/html')
    
    def test_ac(self):
        res = self.testapp.get('/api/SampleYear', status=200)
        self.assertEqual(res.content_type, 'application/json')

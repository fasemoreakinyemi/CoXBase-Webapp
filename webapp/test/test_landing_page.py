import sys
sys.path.append("..")
import unittest

from pyramid import testing


class LandingpageViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_landing_page(self):
        from views.landing_page import my_view 

        request = testing.DummyRequest()
        response = my_view(request)
        self.assertEqual(response, {'status': "Log in", 'route': 'login'})

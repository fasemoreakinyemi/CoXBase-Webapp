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
        from views.help import help_page

        request = testing.DummyRequest()
        response = help_page(request)
        self.assertEqual(response, {})

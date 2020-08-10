import sys
sys.path.append("..")
import unittest

from pyramid import testing


class LandingpageViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_isolate_query_page(self):
        from views.isolate_query import isolate_query_view

        request = testing.DummyRequest()
        response = isolate_query_view(request)
        self.assertEqual(response, {})

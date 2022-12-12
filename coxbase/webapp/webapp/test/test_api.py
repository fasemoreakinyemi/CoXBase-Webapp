import sys

sys.path.append("..")
import unittest

from pyramid import testing


class APIFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import get_app

        app = get_app("../../development.ini")
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_year_response(self):
        res = self.testapp.get("/api_country/DE", status=200)
        self.assertEqual(res.content_type, "application/json")
        self.assertIn("2005", res.json)

    def test_host_response(self):
        res = self.testapp.get("/api_host/DE", status=200)
        self.assertEqual(res.content_type, "application/json")
        self.assertIn("cattle", res.json)

    def test_province_response(self):
        res = self.testapp.get("/api_province/DE", status=200)
        self.assertEqual(res.content_type, "application/json")
        self.assertIn("NW", res.json)

    def test_genotype_response(self):
        res = self.testapp.get("/api_genotype/DE", status=200)
        self.assertEqual(res.content_type, "application/json")
        self.assertIn("A2", res.json)

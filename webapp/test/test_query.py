import os

import unittest

from pyramid import testing


class QueryFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import get_app

        app = get_app("{}/webapp/development.ini".format(os.environ["TRAVIS_BUILD_DIR"]))
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_MLVA_response(self):
        res = self.testapp.get("/fp_query/4/7/11.5/6/6/3/9/9/3/3/5/2/4/4", status=200)
        self.assertEqual(res.content_type, "application/json")
        self.assertEqual(res.json[0]["Genotype"], "A1")

    def test_MST_response(self):
        res = self.testapp.get("/mst_query/4/6/3/5/6/2/8/2/5/6", status=200)
        self.assertEqual(res.content_type, "application/json")
        self.assertEqual(res.json[0]["MST ID"], 5)


import os

import unittest

from pyramid import testing


class GenotypingResultsTests(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import get_app

        app = get_app("{}/development.ini".format(os.environ["TRAVIS_BUILD_DIR"]))
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_MLVA_result_positive(self):
        res = self.testapp.get("/result/mlva/3153d982a498460799263d1d9587ecf6", status=200)
        self.assertEqual(res.content_type, "text/html")
    
    def test_MLVA_result_negative(self):
        res = self.testapp.get("/result/mlva/3153d982af6", status=404)
        self.assertEqual(res.content_type, "text/html")

    def test_MST_result_positive(self):
        res = self.testapp.get("/result/mst/83df27f3c5c7467682a3fb18b7ef3ef6", status=200)
        self.assertEqual(res.content_type, "text/html")
    
    def test_MST_result_negative(self):
        res = self.testapp.get("/result/mst/3153d982af6", status=404)
        self.assertEqual(res.content_type, "text/html")
    
    def test_adaA_result_positive(self):
        res = self.testapp.get("/result/adaA/4d14521570f94f58a5c818d82211666a", status=200)
        self.assertEqual(res.content_type, "text/html")
    
    def test_adaA_result_negative(self):
        res = self.testapp.get("/result/adaA/3153d982af6", status=404)
        self.assertEqual(res.content_type, "text/html")
    
    def test_is1111_result_positive(self):
        res = self.testapp.get("/result/is1111/41533def4e044cfd8d111171b3251ad4", status=200)
        self.assertEqual(res.content_type, "text/html")
    
    def test_is1111_result_negative(self):
        res = self.testapp.get("/result/is1111/3153d982af6", status=404)
        self.assertEqual(res.content_type, "text/html")



#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append("/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp")
sys.path.append("..")
import unittest

print(sys.path)
from pyramid import testing


class AnalysespageViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_mlvaanalysis(self):
        from views.analyses_page import mlvaanalysis_view

        request = testing.DummyRequest()
        response = mlvaanalysis_view(request)
        self.assertEqual(response, {})
    
    def test_mstanalysis(self):
        from views.analyses_page import mstanalysis_view

        request = testing.DummyRequest()
        response = mstanalysis_view(request)
        self.assertEqual(response, {})
    
    def test_is1111analysis(self):
        from views.analyses_page import is1111analysis_view

        request = testing.DummyRequest()
        response = is1111analysis_view(request)
        self.assertEqual(response, {})
    
    def test_adaAanalysis(self):
        from views.analyses_page import adaAanalysis_view

        request = testing.DummyRequest()
        response = adaAanalysis_view(request)
        self.assertEqual(response, {})


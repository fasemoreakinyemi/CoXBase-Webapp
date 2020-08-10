#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import unittest
import sys
sys.path.append("..")
print(sys.path)
from pyramid import testing

class adaATest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_mlva_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.mlva_analysis import mlvaprocess_view
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        self.assertRaises(HTTPNotFound, mlvaprocess_view, request)
    
    def test_subMLVA_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.mlva_analysis import subMLVA_view
        request = testing.DummyRequest(matchdict={'ID':"degrjnifjne"})
        self.assertRaises(HTTPNotFound, subMLVA_view, request)

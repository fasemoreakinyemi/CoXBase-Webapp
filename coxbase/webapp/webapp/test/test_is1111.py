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

    def test_is1111_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.is1111_analysis import is1111process_view
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        self.assertRaises(HTTPNotFound, is1111process_view, request)
    
    def test_resis1111_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.is1111_analysis import resis1111_view
        request = testing.DummyRequest(matchdict={'ID':"degrjnifjne"})
        self.assertRaises(HTTPNotFound, resis1111_view, request)

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

    def test_mst_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.mst_analysis import mstprocess_view
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        self.assertRaises(HTTPNotFound, mstprocess_view, request)
    
    def test_resMST_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.mst_analysis import resMST_view
        request = testing.DummyRequest(matchdict={'ID':"degrjnifjne"})
        self.assertRaises(HTTPNotFound, resMST_view, request)
    
    def test_subMST_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.mst_analysis import subMST_view
        request = testing.DummyRequest(matchdict={'ID':"degrjnifjne"})
        self.assertRaises(HTTPNotFound, subMST_view, request)
    
    def test_phlMST_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.mst_analysis import phlMST_view
        request = testing.DummyRequest(matchdict={'ID':"degrjnifjne"})
        self.assertRaises(HTTPNotFound, phlMST_view, request)

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

    def test_hornstra_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.snp_hornstra import processHornstra_view
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        self.assertRaises(HTTPNotFound, processHornstra_view, request)
    
    def test_resHornstra_forbidden(self):
        from pyramid.httpexceptions import HTTPNotFound
        from views.snp_hornstra import resHornstra_view
        request = testing.DummyRequest(matchdict={'ID':"degrjnifjne"})
        self.assertRaises(HTTPNotFound, resHornstra_view, request)

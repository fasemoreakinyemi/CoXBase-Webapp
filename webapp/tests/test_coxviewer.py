#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append("..")
import unittest

from pyramid import testing


class CoxviewerViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_cox_map(self):
        from views.coxviewer import coxmap_view

        request = testing.DummyRequest()
        response = coxmap_view(request)
        self.assertEqual(response, {'status': "Log in", 'route': 'login'})
    
    def test_coxviewer_table(self):
        from views.coxviewer import coxtable_view

        request = testing.DummyRequest()
        response = coxtable_view(request)
        self.assertEqual(response, {})


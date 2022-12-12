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

    def test_sequenceviewer(self):
        from views.sequenceviewer import sequence_view

        request = testing.DummyRequest()
        response = sequence_view(request)
        self.assertEqual(response, {})

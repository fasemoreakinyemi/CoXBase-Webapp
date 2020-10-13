#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append("..")
import unittest
import uuid
from pathlib import Path
from io import StringIO
from pyramid import testing
import os
import configparser


config = configparser.ConfigParser()
config.read("/home/ubuntu/coxbase/coxbase/webapp/webapp/views_processor/paths_config.ini")
sole_outpath = config['OUTPATH']['sole']
combined_outpath = config['OUTPATH']['combined']


class CoxviewerViewTests(unittest.TestCase):
    def setUp(self):
        from newick_generator import NewickProcessor
        self.config = testing.setUp()
        self.mock_data = Mock_data()
        self.input_file = config['TESTDATA']['fasta']
        self.np = NewickProcessor()

    def tearDown(self):
        testing.tearDown()

    
    def test_schriver_distance(self):
        from newick_generator import NewickProcessor
        np = NewickProcessor()
        dist = np.shriver_distance(self.mock_data.shriver_data[0],
                                   self.mock_data.shriver_data[1])
        self.assertEquals(dist, 0.0)
    
    def test_distance_matric(self):
        matric = self.np.distance_matric(self.mock_data.shriver_data)
        self.assertEquals(matric, 0.0)
    
    def test_generate_newick(self):
        newick = self.np.generate_newick(self.mock_data.shriver_data,
                                        self.mock_data.index)
        print(type(newick))
        self.assertEquals(newick, "(b:0.000000,a:0.000000);")
    

class Mock_data():
    shriver_data = [[11,22,10,23,5,5,3,5,4,7],[11,22,10,23,5,5,3,5,4,7]]
    index = ["a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j"]

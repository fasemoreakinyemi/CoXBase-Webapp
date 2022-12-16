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
config.read(os.path.join(os.path.dirname("__file__"), "paths_config.ini"))
sole_outpath = config['OUTPATH']['sole']
combined_outpath = config['OUTPATH']['combined']


class CoxviewerViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.mock_data = Mock_data()
        self.input_file = "./test.fasta"

    def tearDown(self):
        testing.tearDown()

    
    def test_create_fasta_file_from_post_object(self):
        from views_processor import ViewProcessor
        vp = ViewProcessor()
        analysis_types = ["sole", "combined"]
        for a_types in analysis_types:
            process_ID = uuid.uuid4().hex 
            file_path = vp.create_file_from_fastafile(open(self.input_file,"rb"),
                                                      process_ID,
                                                      a_types)
            self.assertEqual(Path(file_path).is_file(), True)
            os.remove(file_path)
    
    def test_create_fasta_file_from_fasta_seq(self):
        from views_processor import ViewProcessor
        vp = ViewProcessor()
        process_ID = uuid.uuid4().hex 
        analysis_types = ["sole"]
        file_path = vp.create_file_from_fastaentry(str.encode(self.mock_data.fasta_seq),
                                                   process_ID)
        self.assertEqual(Path(file_path).is_file(), True)
        os.remove(file_path)
    
    def test_create_e_pcr_command_mlva(self):
        from views_processor import ViewProcessor
        vp = ViewProcessor()
        process_ID = uuid.uuid4().hex 
        analysis_types = ["sole"]
        command = vp.create_epcr_command(self.input_file,
                                        process_ID,
                                        analysis_types[0],
                                        "mlva",
                                        )
        self.assertEqual(command[8], config['STSPATH']['mlva'])

    def test_create_e_pcr_command_is1111(self):
        from views_processor import ViewProcessor
        vp = ViewProcessor()
        process_ID = uuid.uuid4().hex 
        analysis_types = ["sole"]
        command = vp.create_epcr_command(self.input_file,
                                        process_ID,
                                        analysis_types[0],
                                        "is1111",
                                        )
        self.assertEqual(command[8], config['STSPATH']['is1111'])

    def test_extract_mlva_values(self):
        from views_processor import ViewProcessor
        vp = ViewProcessor()
        process_ID = "f34897bd5d96419e945d84dc04d642db" 
        analysis_types = ["sole"]
        value_dict = vp.extract_mlva_values(process_ID,
                                        analysis_types[0],
                                        )
        self.assertEqual(value_dict['product']['ms01'],
                             '248')
    
    def test_extract_is1111_values(self):
        from views_processor import ViewProcessor
        vp = ViewProcessor()
        process_ID = "314dc52a80d94ac38a03376dc419281e" 
        analysis_types = ["sole"]
        value_dict = vp.extract_is1111_values(process_ID,
                                        analysis_types[0],
                                        )
        self.assertEqual(value_dict['IS1111_4'],
                             1)
    
    def test_mstprocessor(self):
        from views_processor import ViewProcessor
        vp = ViewProcessor()
        process_ID = uuid.uuid4().hex 
        analysis_types = ["sole"]
        spacer = vp.mstprocessor(self.input_file,
                                 process_ID,
                                 analysis_types[0])
        self.assertEqual(spacer['cox56'], 90)
    
    def test_adaprocessor(self):
        from views_processor import ViewProcessor
        vp = ViewProcessor()
        process_ID = uuid.uuid4().hex 
        analysis_types = ["sole"]
        typing_dict = vp.adaprocessor(self.input_file,
                                      process_ID,
                                      analysis_types[0])
        print(typing_dict)
        self.assertEqual(typing_dict['plasmidType'], 'QpDG')
    
    def test_Hornstraprocessor(self):
        from views_processor import ViewProcessor
        vp = ViewProcessor()
        process_ID = uuid.uuid4().hex 
        analysis_types = ["sole"]
        typing_dict = vp.snpHornstraprocessor(self.input_file,
                                              process_ID)
        print(typing_dict)
        self.assertEqual(typing_dict['Cox18bp376'], 'G')

class Mock_data():
    fasta_seq = """>test_1 a random sequence
    TTTAGAAATTACACAACGAGAAATTAAATTAAATTTAGAGACATTGGATTTTATT"""


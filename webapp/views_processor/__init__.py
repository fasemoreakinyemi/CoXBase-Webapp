#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from .. import models
from pyramid.response import Response
import pandas as pd
import numpy as np
import os
import uuid
import shutil
import json
from pathlib2 import Path
import pyfastcopy
from Bio import pairwise2, SeqIO
import subprocess


class ViewProcessor():

    @staticmethod
    def create_file_from_fastafile(inputfile, process_ID):
        file_path = os.path.join('/home/ubuntu/temp/','{}.fasta'.format(process_ID))
        temp_file_path = file_path
        inputfile.seek(0)
        with open(temp_file_path, 'wb') as output_file:
            shutil.copyfileobj(inputfile, output_file)
        os.rename(temp_file_path, file_path)
        return file_path
    
    @staticmethod
    def create_file_from_fastaentry(sequence, process_ID):
        file_path = os.path.join('/home/ubuntu/temp/','{}.fasta'.format(process_ID))
        with open(file_path, "wb") as output_file:
            output_file.write(sequence)
        output_file.close()
        return file_path
    
    @staticmethod
    def create_epcr_command(file_path, process_ID):
        out_file = "/home/ubuntu/temp/epcr_{}_output.tab".format(process_ID)
        Path(out_file).touch()
        sts_file = "/home/ubuntu/coxbase/coxbase/scripts/input/coxiella_ms.sts"
        command = ["/home/ubuntu/tools/Linux-x86_64/e-PCR", "-w7", "-f","1","-m100","-o", out_file,"-t3", sts_file, file_path]
        return command

    @staticmethod
    def extract_mlva_values(process_ID):
        flank_len_dict = {"ms01": 176, "ms03": 142,
                  "ms20": 96, "ms21": 137,
                  "ms22": 174, "ms23": 91,
                  "ms24": 126, "ms26": 97,
                  "ms28": 107, "ms27": 249,
                  "ms30": 199, "ms31": 99,
                  "ms33": 193, "ms34": 168}
        repeat_size_dict = {"ms01": 16, "ms03": 12,
                  "ms20": 33, "ms21": 12,
                  "ms22": 11, "ms23": 7,
                  "ms24": 7, "ms26": 9,
                  "ms28": 6, "ms27": 6,
                  "ms30": 18, "ms31": 7,
                  "ms33": 7, "ms34": 6}

        out_file = "/home/ubuntu/temp/epcr_{}_output.tab".format(process_ID)
        epcr_df = pd.read_table(out_file, sep="\t", header=None)
        header = ["id", "ms_id", "strand", "start", "end", "length", "un1",
          "un2", "desc"]
        epcr_df.columns = header
        prod_dict = pd.Series(epcr_df.length.values,
                      index=epcr_df.ms_id).to_dict()
        out_prod_dict = {'ID': process_ID}
        out_repeat_dict = {'ID': process_ID}
        out_flnk_dict = {'ID': process_ID}
        out_rsize_dict = {'ID': process_ID}
        new_list = []
        for keys in flank_len_dict:
            prod = prod_dict.get(keys, None)
            if prod is not None:
                prod = prod.split("/")[0]
                out_prod_dict[keys] = prod
                flank_len = flank_len_dict[keys]
                out_flnk_dict[keys] = flank_len
                rep_size = repeat_size_dict[keys]
                out_rsize_dict[keys] = rep_size
                repeat_num = float((int(prod) - int(flank_len))/ int(rep_size))
                repeat_num2 = int((int(prod) - int(flank_len))/ int(rep_size))
                out_repeat_dict[keys] = repeat_num2
        values_dict = {"product" : out_prod_dict,
                       "repeat" : out_repeat_dict,
                       "repeatSize" : out_rsize_dict,
                       "flank" :  out_flnk_dict}
        return values_dict

    @staticmethod
    def mstprocessor(file_path, process_ID):
        os.mkdir("/home/ubuntu/temp/{}".format(process_ID))
        spacer_dict = {"ID": process_ID}
        primer_dict = {
            "cox18" : ["CGCAGACGAATTAGCCAATC","TTCGATGATCCGATGGCCTT"],
            "cox2" : ["CAACCCTGAATACCCAAGGA","GAAGCTTCTGATAGGCGGGA"],
            "cox20" : ["GATATTTATCAGCGTCAAAGCAA","TCTATTATTGCAATGCAAGTGG"],
            "cox22" : ["GGGAATAAGAGAGTTAGCTCA","CGCAAATTTCGGCACAGACC"],
            "cox37" : ["GGCTTGTCTGGTGTAACTGT","ATTCCGGGACCTTCGTTAAC"],
            "cox5" : ["CAGGAGCAAGCTTGAATGCG","TGGTATGACAACCCGTCATG"],
            "cox51" : ["TAACGCCCGAGAGCTCAGAA","GCGAGAACCGAATTGCTATC"],
            "cox56" : ["CCAAGCTCTCTGTGCCCAAT","ATGCGCCAGAAACGCATAGG"],
            "cox57" : ["TGGAAATGGAAGGCGGATTC","GGTTGGAAGGCGTAAGCCTTT"],
            "cox61" : ["GAAGATAGAGCGGCAAGGAT","GGGATTTCAACTTCCGATAGA"]}

        for key, value in primer_dict.items():
            spacer = key
            fwd_prim = value[0]
            rev_prim = value[1]
            out_file = os.path.join("/home/ubuntu/temp/{}".format(process_ID),
                                    "{}.fasta".format(spacer))
            command = ["/home/ubuntu/tools/usearch",
                   "-search_pcr2",file_path,"-fwdprimer", fwd_prim, "-revprimer",
                   rev_prim,"-strand", "both", "-fastaout", out_file]
            subprocess.call(command)
            db = SeqIO.parse("/home/ubuntu/db/{}.fa".format(spacer), "fasta")
            spacer_fasta = SeqIO.read(out_file, "fasta")
            for records in db:
                len_records = len(records.seq)
                if len_records == len(spacer_fasta.seq):
                    alignments = pairwise2.align.globalxs(records.seq, spacer_fasta.seq.upper(), -2,-1, score_only=True)
                    if alignments == len_records:
                        spacer_id = records.id.split(".")[1]
                        spacer_dict[spacer] = spacer_id
        return spacer_dict

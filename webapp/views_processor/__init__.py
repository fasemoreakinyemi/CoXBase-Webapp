#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
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
import configparser


config = configparser.ConfigParser()
config.read("/home/travis/build/foerstner-lab/CoxBase-Webapp/webapp/views_processor/paths_config.ini")
sole_outpath = config['OUTPATH']['sole']
combined_outpath = config['OUTPATH']['combined']

class ViewProcessor:
    @staticmethod
    def create_file_from_fastafile(inputfile, process_ID, analysis_type):
        if analysis_type == "sole":
            file_path = os.path.join(sole_outpath, "{}.fasta".format(process_ID))
        else:
            os.mkdir("{}/{}".format(combined_outpath, process_ID))
            file_path = os.path.join(
                "{}/{}".format(combined_outpath, process_ID),
                "{}.fasta".format(process_ID),
            )
        temp_file_path = file_path
        inputfile.seek(0)
        with open(temp_file_path, "wb") as output_file:
            shutil.copyfileobj(inputfile, output_file)
        os.rename(temp_file_path, file_path)
        return file_path
    
    @staticmethod
    def create_file_from_fastaentry(sequence, process_ID):
        file_path = os.path.join(sole_outpath, "{}.fasta".format(process_ID))
        with open(file_path, "wb") as output_file:
            output_file.write(sequence)
        output_file.close()
        return file_path

    @staticmethod
    def create_epcr_command(file_path, process_ID, analysis_type, analysis_name):
        sts_file = {"mlva": config['STSPATH']['mlva'],
                    "is1111": config['STSPATH']['is1111']}[analysis_name]
        if analysis_type == "sole":
            out_file = "{}/epcr_{}_output.tab".format(sole_outpath, process_ID)
        else:
            if analysis_name == "mlva":
                out_file = "{}/{}/epcr_mlva_{}_output.tab".format(combined_outpath,
                                                                  process_ID,
                                                                  process_ID
                                                                 )
            if analysis_name == "is1111":
                out_file = "{}/{}/epcr_is1111_{}_output.tab".format(combined_outpath,
                                                                    process_ID,
                                                                    process_ID
                                                                    )


        Path(out_file).touch()
        command = [
            config['ExternalToolsPATH']['epcr'],
            "-w5",
            "-f",
            "2",
            "-n1",
            "-g1",
            "-u+",
            "-d 50-1600",
            "-o",
             out_file,
            "-t3",
            sts_file,
            file_path]
        return command

    @staticmethod
    def extract_mlva_values(process_ID, analysis_type):
        flank_len_dict = {
            "ms01": 176,
            "ms03": 142,
            "ms20": 96,
            "ms21": 136,
            "ms22": 174,
            "ms23": 90,
            "ms24": 135,
            "ms26": 104,
            "ms28": 112,
            "ms27": 249,
            "ms30": 205,
            "ms31": 106,
            "ms33": 193,
            "ms34": 175,
        }
        repeat_size_dict = {
            "ms01": 16,
            "ms03": 12,
            "ms20": 33,
            "ms21": 12,
            "ms22": 11,
            "ms23": 7,
            "ms24": 7,
            "ms26": 9,
            "ms28": 6,
            "ms27": 6,
            "ms30": 18,
            "ms31": 7,
            "ms33": 7,
            "ms34": 6,
        }

        if analysis_type == "sole":
            result_file = "{}/epcr_{}_output.tab".format(sole_outpath, process_ID)
        else:
            result_file = "{}/{}/epcr_mlva_{}_output.tab".format(combined_outpath,
                                                                 process_ID,
                                                                 process_ID
                                                                 )

        epcr_df = pd.read_table(result_file, sep="\t", header=None)
        header = [
            "id",
            "ms_id",
            "strand",
            "start",
            "end",
            "length",
            "un1",
            "un2",
            "desc",
        ]
        epcr_df.columns = header
        prod_dict = pd.Series(epcr_df.length.values, index=epcr_df.ms_id).to_dict()
        out_prod_dict = {"ID": process_ID}
        out_repeat_dict = {"ID": process_ID}
        out_flnk_dict = {"ID": process_ID}
        out_rsize_dict = {"ID": process_ID}
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
                repeat_num = float((int(prod) - int(flank_len)) / int(rep_size))
                repeat_num2 = int((int(prod) - int(flank_len)) / int(rep_size))
                out_repeat_dict[keys] = repeat_num2
        values_dict = {
            "product": out_prod_dict,
            "repeat": out_repeat_dict,
            "repeatSize": out_rsize_dict,
            "flank": out_flnk_dict,
        }
        return values_dict


    @staticmethod
    def extract_is1111_values(process_ID, analysis_type):
        element_list = [
            "IS1111_1",
            "IS1111_2",
            "IS1111_3",
            "IS1111_4",
            "IS1111_5",
            "IS1111_6",
            "IS1111_7",
            "IS1111_8",
            "IS1111_9",
            "IS1111_10",
            "IS1111_11",
            "IS1111_12",
            "IS1111_13",
            "IS1111_14",
            "IS1111_15",
            "IS1111_16",
            "IS1111_17",
            "IS1111_18",
            "IS1111_19",
            "IS1111_20",
            "IS1111_21",
            "IS1111_22",
            "IS1111_23",
            "IS1111_24",
            "IS1111_25",
            "IS1111_26",
            "IS1111_27",
            "IS1111_28",
            "IS1111_29",
            "IS1111_30",
            "IS1111_31",
            "IS1111_32",
            "IS1111_33",
            "IS1111_34",
            "IS1111_35",
            "IS1111_36",
            "IS1111_37",
            "IS1111_38",
            "IS1111_39",
            "IS1111_40",
            "IS1111_41",
            "IS1111_42",
            "IS1111_43",
            "IS1111_44",
            "IS1111_45",
            "IS1111_46",
            "IS1111_47",
            "IS1111_48",
            "IS1111_49",
            "IS1111_50",
            "IS1111_51",
            "IS1111_53",
            "IS1111_54",
            "IS1111_55",
            "IS1111_56",
            "IS1111_57",
            "IS1111_58",
            "IS1111_59",
            "IS1111_60",
            "IS1111_61",
            "IS1111_84",
        ]
        if analysis_type == "sole":
            result_file = "{}/epcr_{}_output.tab".format(sole_outpath,
                                                         process_ID)
        else:
            result_file = "{}/{}/epcr_is1111_{}_output.tab".format(combined_outpath,
                                                                   process_ID,
                                                                   process_ID
                                                                   )

        epcr_df = pd.read_table(result_file, sep="\t", header=None)
        header = [
            "id",
            "is_id",
            "strand",
            "start",
            "end",
            "length",
            "un1",
            "un2",
            "desc",
        ]
        epcr_df.columns = header
        detected_element_list = epcr_df.is_id.tolist()
        detected_element_dict = {"ID": process_ID}
        for element in element_list:
            if element in detected_element_list:
                detected_element_dict[element] = 1
            else:
                detected_element_dict[element] = 0
        return detected_element_dict

    @staticmethod
    def mstprocessor(file_path, process_ID, analysis_type):
        if analysis_type == "sole":
            output_dir = "{}/{}".format(sole_outpath,
                                        process_ID)
        else:
            output_dir = "{}/{}/mst".format(combined_outpath,
                                            process_ID)
        os.mkdir(output_dir)
        spacer_dict = {"ID": process_ID}
        primer_dict = {
            "cox18": ["CGCAGACGAATTAGCCAATC", "TTCGATGATCCGATGGCCTT"],
            "cox2": ["CAACCCTGAATACCCAAGGA", "GAAGCTTCTGATAGGCGGGA"],
            "cox20": ["GATATTTATCAGCGTCAAAGCAA", "TCTATTATTGCAATGCAAGTGG"],
            "cox22": ["GGGAATAAGAGAGTTAGCTCA", "CGCAAATTTCGGCACAGACC"],
            "cox37": ["GGCTTGTCTGGTGTAACTGT", "ATTCCGGGACCTTCGTTAAC"],
            "cox5": ["CAGGAGCAAGCTTGAATGCG", "TGGTATGACAACCCGTCATG"],
            "cox51": ["TAACGCCCGAGAGCTCAGAA", "GCGAGAACCGAATTGCTATC"],
            "cox56": ["CCAAGCTCTCTGTGCCCAAT", "ATGCGCCAGAAACGCATAGG"],
            "cox57": ["TGGAAATGGAAGGCGGATTC", "GGTTGGAAGGCGTAAGCCTTT"],
            "cox61": ["GAAGATAGAGCGGCAAGGAT", "GGGATTTCAACTTCCGATAGA"],
        }

        for key, value in primer_dict.items():
            spacer = key
            fwd_prim = value[0]
            rev_prim = value[1]
            out_file = os.path.join(output_dir, "{}.fasta".format(spacer))
            command = [
                config['ExternalToolsPATH']['usearch'],
                "-search_pcr2",
                file_path,
                "-fwdprimer",
                fwd_prim,
                "-revprimer",
                rev_prim,
                "-strand",
                "both",
                "-fastaout",
                out_file,
            ]
            subprocess.call(command)
            db = SeqIO.parse(
                "{}/{}.fa".format(config['MSTLIBPATH']['db'],
                                  spacer),
                "fasta"
                           )  # open MST library
            try:
                spacer_fasta = SeqIO.read(out_file, "fasta")
            except:
                pass
            if spacer_fasta:
                spacer_id = ""
                for records in db:
                    len_records = len(records.seq)
                    if len_records == len(spacer_fasta.seq):
                        alignments = pairwise2.align.globalxs(
                            records.seq,
                            spacer_fasta.seq.upper(),
                            -2,
                            -1,
                            score_only=True,
                        )
                        if alignments == len_records:  # check for mismatch
                            spacer_id = records.id.split(".")[1]
                            spacer_dict[spacer] = spacer_id
                if spacer_id == "":
                    spacer_dict[spacer] = 90
        return spacer_dict


    @staticmethod
    def adaprocessor(file_path, process_ID, analysis_type):
        if analysis_type == "sole":
            output_dir = "{}/{}".format(sole_outpath,
                                        process_ID)
        else:
            output_dir = "{}/{}/ada".format(combined_outpath,
                                            process_ID)
        os.mkdir(output_dir)
        typing_dict = {"ID": process_ID}
        primer_dict = {
            "adaA": ["AGGAGGAGGTCACTTGAAAAAACTA", "AACTTTTCTAGCGTTATTTGCCTAT"],
            "QpH1": ["TGACAAATAGAATTTCTTCATTTTGATG", "GCTTATTTTCTTCCTCGAATCTATGAAT"],
            "QpRS": ["CTCGTACCCAAAGACTATGAATATATCC", "CACATTGGGTATCGTACTGTCCCT"],
            "QpDG": ["ggCgAggTgTTCggTATgAG", "CTTAgCgATTTATggTTCCgTC"],
            "QpDV": ["CTTATTTCAAAgAgTTCCTgCTAg", "CgCAACCggCTgTTgTgC"],
        }

        for key, value in primer_dict.items():
            fwd_prim = value[0]  # forward primer
            rev_prim = value[1]  # reverse primer
            out_file = os.path.join(
                output_dir, "{}.fasta".format(key)
            )
            command = [
                config['ExternalToolsPATH']['usearch'],
                "-search_pcr2",
                file_path,
                "-fwdprimer",
                fwd_prim,
                "-revprimer",
                rev_prim,
                "-strand",
                "both",
                "-fastaout",
                out_file,
            ]
            subprocess.call(command)
            if key == "adaA":
                if os.stat(out_file).st_size == 0:  # check if file is empty
                    typing_dict["adaAStatus"] = 0  # 0 for AdaA gene negative
                    typing_dict["genotype"] = "Q212 or Q154 Del"
                else:
                    typing_dict["adaAStatus"] = 1  # 1 for AdaA gene positive
                    read_fasta = SeqIO.read(out_file, "fasta")
                    if len(read_fasta.seq) == 668:
                        if read_fasta.seq[418].upper() == "A":
                            typing_dict["genotype"] = "wildtype"
                        elif read_fasta.seq[418].upper() == "T":
                            typing_dict["genotype"] = "A431T SNP"
                    else:
                        if len(read_fasta.seq) > 668:
                            typing_dict["genotype"] = "repeat"
                        else:
                            typing_dict["genotype"] = "incomplete"

            else:
                if os.stat(out_file).st_size == 0:
                    continue
                else:
                    typing_dict["plasmidType"] = key
        return typing_dict

    
    @staticmethod
    def snpHornstraprocessor(file_path, process_ID):
        os.mkdir("{}/{}".format(sole_outpath,
                                process_ID))
        typing_dict = {"ID": process_ID}
        primer_dict = {
            "Cox5bp81": ["CGAGGTGTTTGGTGTGTTGAA", "GGAGAGGGACAATACGTGCTTATG", 48],
            "Cox22bp91": ["GGTGAATAGATTACGCCTTCCATT", "CGCCTTATGTAATTGTCGTTCAAT", 42],
            "Cox18bp376": ["CAGCGCCTCCCTTTTTT", "GCTTAAGTTGGCGCTTCTGTG", 1],
            "Cox51bp356": ["GTATCTGCTAAAAAGCTAGCGAAA", "GACTTTATCATCGCCCGGTAG", 1],
            "Cox18bp34": ["GCTTTAAATTTTTGATAGGGGTATAACTA", "CGAATTAGCCAATCGTGGC", 1],
            "Cox5bp109": ["TGATATGCTTAACATAAGCACGTATT", "CTCTCCTTAACCCTCTCCTCGA", 1],
            "Cox22bp118": ["GTGCGGAGAAAATATTGAACG", "CGCTAAGCAAAAAGTGAGTGATAGC", 1],
            "Cox51bp492": ["TCAATTTTTCAAGCGGCATA", "GACGGGATAAGTCGGGAGG", 1],
            "Cox57bp327": ["GATAACAAGCTTTATTTGCCGACT", "ATCAGTTAGTCAGATATCTTTAATTTTAATCGG", 1],
            "Cox56bp10": ["ATAGTCTTAGCTCTGATTGCAACA", "CAAGCTCTCTGTGCCCAAT", 1],
            "Cox51bp67": ["GTTGAGAGAATAGTGGGTTTTACTAAT", "TTATCGTACGA", 2],
            "Cox20bp155": ["GGTATTCAAGGCTTGTGAGATAAAC", "CAGGTTCAGCGATTGCATTAG", 1]
        }

        for key, value in primer_dict.items():
            fwd_prim = value[0]  # forward primer
            rev_prim = value[1]  # reverse primer
            out_file = os.path.join("{}/{}".format(sole_outpath, process_ID),
                                    "{}.fasta".format(key)
            )
            command = [
                config['ExternalToolsPATH']['usearch'],
                "-search_pcr2",
                file_path,
                "-fwdprimer",
                fwd_prim,
                "-revprimer",
                rev_prim,
                "-strand",
                "both",
                "-fastaout",
                out_file,
            ]
            subprocess.call(command)
            if os.stat(out_file).st_size == 0:  # check if file is empty
                    typing_dict[key] = 0  # 0 for AdaA gene negative
            else:
                read_fasta = list(SeqIO.parse(out_file, "fasta"))
                typing_dict[key] = read_fasta[0].seq[value[2]].upper()
        return typing_dict


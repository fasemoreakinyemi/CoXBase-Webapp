from pyramid.view import view_config
from sqlalchemy.sql import insert
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )
from pyramid.httpexceptions import HTTPBadRequest
from pathlib2 import Path
from .. import models
import argparse
import pandas as pd
import subprocess
import os
import uuid
import shutil
import json
from Bio import pairwise2, SeqIO

@view_config(route_name='mstresult')
def mstprocess_view(request):
    spacer_dict = {}
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

    if 'fastafile' not in request.POST or 'fastaentry' not in request.POST:
        raise HTTPNotFound()
    filename = request.POST['fastafile'].filename
    inputfile = request.POST['fastafile'].file
    process_ID = uuid.uuid4().hex
    spacer_dict["ID"] = process_ID
    wd = os.mkdir("/home/ubuntu/temp/{}".format(process_ID))
    file_path = os.path.join('/home/ubuntu/temp/{}/'.format(process_ID),'{}.fasta'.format(process_ID))
    temp_file_path = file_path
    inputfile.seek(0)
    with open(temp_file_path, 'wb') as output_file:
        shutil.copyfileobj(inputfile, output_file)
    os.rename(temp_file_path, file_path)
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
    submission_dict = {'ID' : process_ID, 
                       'AnalysisType': 'MST Insilico typing',
                       'IPaddress' : request.remote_addr} 
    session = request.db2_session
    session.execute(insert(models.SubmissionTable).values([submission_dict]))
    session.execute(insert(models.mstSpacerResult).values([spacer_dict]))
    session.commit()
    url = request.route_url('resMST', ID=process_ID)
    return HTTPFound(location=url)

@view_config(route_name='resMST',
             renderer="../templates/mst_analysis_result_table.jinja2")
def resMST_view(request):
    process_ID = request.matchdict['ID']
    query = request.db2_session.query(models.mstSpacerResult).filter(
        models.mstSpacerResult.ID == process_ID).first()
    if query is None:
        raise HTTPNotFound()
    return  {'results' :query}

#@view_config(route_name='subMLVA',
#             renderer="../templates/mlva_analysis_submission_table.jinja2")
#def subMST_view(request):
#    process_ID = request.matchdict['ID']
#    query = request.db2_session.query(models.SubmissionTable).filter(
#        models.SubmissionTable.ID == process_ID).first()
#    if query is None:
#        raise HTTPNotFound()
#    return  {'submission' :query }



@view_config(route_name='phlMST',
             renderer="../templates/mst_analysis_phylogenetics.jinja2")
def phlMST_view(request):
    process_ID = request.matchdict['ID']
    query = request.db2_session.query(models.mstSpacerResult).filter(
        models.mstSpacerResult.ID == process_ID).first()
    if query is None:
        raise HTTPNotFound()
    return  {'results' :query }




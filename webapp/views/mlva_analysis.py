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

#def is_fasta(filename):
#    with open(filename, "rU") as handle:
#        fasta = SeqIO.parse(handle, "fasta")
#        return any(fasta)

@view_config(route_name='mlvaresult')
def mlvaprocess_view(request):
    if 'fastafile' not in request.POST or 'fastaentry' not in request.POST:
        raise HTTPNotFound()
    filename = request.POST['fastafile'].filename
    inputfile = request.POST['fastafile'].file
    process_ID = uuid.uuid4().hex
    file_path = os.path.join('/home/ubuntu/temp/','{}.fasta'.format(process_ID))
    temp_file_path = file_path
    inputfile.seek(0)
    with open(temp_file_path, 'wb') as output_file:
        shutil.copyfileobj(inputfile, output_file)
    os.rename(temp_file_path, file_path)
    out_file = "/home/ubuntu/temp/output.tab"
    Path(out_file).touch()
    sts_file = "/home/ubuntu/coxbase/coxbase/scripts/input/coxiella_ms.sts"
    command = ["/home/ubuntu/tools/Linux-x86_64/e-PCR", "-w7", "-f","1","-m100","-o", out_file,"-t3", sts_file, file_path]
    subprocess.call(command)
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
    submission_dict = {'ID' : process_ID, 
                       'AnalysisType': 'MLVA Insilico typing',
                       'IPaddress' : request.remote_addr} 
    session = request.db2_session
    session.execute(insert(models.SubmissionTable).values([submission_dict]))
    session.execute(insert(models.ProductLength).values([out_prod_dict]))
    session.execute(insert(models.RepeatSize).values([out_rsize_dict]))
    session.execute(insert(models.RepeatNumber).values([out_repeat_dict]))
    session.execute(insert(models.FlankLength).values([out_flnk_dict]))
    session.commit()
    url = request.route_url('resMLVA', ID=process_ID)
    return HTTPFound(location=url)
@view_config(route_name='resMLVA',
             renderer="../templates/mlva_analysis_result_table.jinja2")
def resMLVA_view(request):
    process_ID = request.matchdict['ID']
    query1 = request.db2_session.query(models.ProductLength).filter(
        models.ProductLength.ID == process_ID).first()
    if query1 is None:
        raise HTTPNotFound()
    query2 = request.db2_session.query(models.FlankLength).filter(
        models.FlankLength.ID == process_ID).first()
    query3 = request.db2_session.query(models.RepeatSize).filter(
        models.RepeatSize.ID == process_ID).first()
    query4 = request.db2_session.query(models.RepeatNumber).filter(
        models.RepeatNumber.ID == process_ID).first()
    return  {'ProductLength' :query1, 'FlankLength': query2, 
             'RepeatSize': query3, 'RepeatNumber': query4}

@view_config(route_name='subMLVA',
             renderer="../templates/mlva_analysis_submission_table.jinja2")
def subMLVA_view(request):
    process_ID = request.matchdict['ID']
    query = request.db2_session.query(models.SubmissionTable).filter(
        models.SubmissionTable.ID == process_ID).first()
    if query is None:
        raise HTTPNotFound()
    return  {'submission' :query }



@view_config(route_name='phlMLVA',
             renderer="../templates/mlva_analysis_phylogenetics.jinja2")
def phlMLVA_view(request):
    process_ID = request.matchdict['ID']
    query = request.db2_session.query(models.RepeatNumber).filter(
        models.RepeatNumber.ID == process_ID).first()
    if query is None:
        raise HTTPNotFound()
    return  {'RepeatNumber' :query }




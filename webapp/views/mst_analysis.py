from pyramid.view import view_config
from sqlalchemy.sql import insert
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    HTTPNotAcceptable)
from pyramid.httpexceptions import HTTPBadRequest
from pathlib2 import Path
from .. import models
import pandas as pd
import subprocess
import os
import uuid
import shutil
import json
import pyfastcopy
from Bio import pairwise2, SeqIO
from .. import views_processor

@view_config(route_name='mstresult')
def mstprocess_view(request):
    VP = views_processor.ViewProcessor()
    if 'fastafile' not in request.POST or 'fastaentry' not in request.POST:
        raise HTTPNotFound()
    filename = ""
    process_ID = uuid.uuid4().hex
    try:
        filename = request.POST['fastafile'].filename
    except:
        pass
    if filename is not "":
        inputfile = request.POST['fastafile'].file
        file_path = VP.create_file_from_fastafile(inputfile, process_ID)
    else:
        sequence = memoryview(request.POST['fastaentry'].encode('utf-8'))
        file_path = VP.create_file_from_fastaentry(sequence, process_ID)
    try:
        spacer_dict = VP.mstprocessor(file_path, process_ID)
    except:
        raise HTTPNotAcceptable("Please check your submission \n Strongly recommend to use a whole genome file")
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

@view_config(route_name='subMST',
             renderer="../templates/mst_analysis_submission_table.jinja2")
def subMST_view(request):
    process_ID = request.matchdict['ID']
    query = request.db2_session.query(models.SubmissionTable).filter(
        models.SubmissionTable.ID == process_ID).first()
    if query is None:
        raise HTTPNotFound()
    return  {'submission' :query }



@view_config(route_name='phlMST',
             renderer="../templates/mst_analysis_phylogenetics.jinja2")
def phlMST_view(request):
    process_ID = request.matchdict['ID']
    query = request.db2_session.query(models.mstSpacerResult).filter(
        models.mstSpacerResult.ID == process_ID).first()
    if query is None:
        raise HTTPNotFound()
    return  {'results' :query }




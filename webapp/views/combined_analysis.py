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
from .. import views_processor


@view_config(route_name='combinedresult')
def combined_result_view(request):
    VP = views_processor.ViewProcessor()
    session = request.db2_session

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
        file_path = VP.create_file_from_fastafile_combined(inputfile, process_ID)
    else:
        sequence = memoryview(request.POST['fastaentry'].encode('utf-8'))
        file_path = VP.create_file_from_fastaentry(sequence, process_ID)
    
    # mlva
    command = VP.create_epcr_command_combined(file_path, process_ID)
    subprocess.call(command)
    mlva_dict = VP.extract_mlva_values_combined(process_ID)
    session.execute(insert(models.ProductLength).values([mlva_dict.get("product")]))
    session.execute(insert(models.RepeatSize).values([mlva_dict.get("repeatSize")]))
    session.execute(insert(models.RepeatNumber).values([mlva_dict.get("repeat")]))
    session.execute(insert(models.FlankLength).values([mlva_dict.get("flank")]))

    # mst
    try:
        spacer_dict = VP.mstprocessor_combined(file_path, process_ID)
    except:
        raise HTTPNotAcceptable("Please check your submission")
    
    session.execute(insert(models.mstSpacerResult).values([spacer_dict]))

    # is1111
    command = VP.create_epcr_command_is1111_combined(file_path, process_ID)
    subprocess.call(command)
    is1111_dict = VP.extract_is1111_values_combined(process_ID)
    session.execute(insert(models.is1111Profile).values([is1111_dict]))

    #ada
    typing_dict = VP.adaprocessor_combined(file_path, process_ID)
    session.execute(insert(models.adaAProfile).values([typing_dict]))
    
    # submission dict
    submission_dict = {'ID' : process_ID, 
                       'AnalysisType': 'comp Insilico typing',
                       'IPaddress' : request.remote_addr} 
    session.execute(insert(models.SubmissionTable).values([submission_dict]))


    session.commit()
    url = request.route_url('resCombined', ID=process_ID)
    return HTTPFound(location=url)

@view_config(route_name='resCombined', renderer="../templates/combined_analysis_result_table.jinja2")
def resCombined_view(request):
    process_ID = request.matchdict['ID']
    return  {'ID' : process_ID}

#@view_config(route_name='subMLVA',
#             renderer="../templates/mlva_analysis_submission_table.jinja2")
#def subMLVA_view(request):
#    process_ID = request.matchdict['ID']
#    query = request.db2_session.query(models.SubmissionTable).filter(
#        models.SubmissionTable.ID == process_ID).first()
#    if query is None:
#        raise HTTPNotFound()
#    return  {'submission' :query }
#
#
#
#@view_config(route_name='phlMLVA',
#             renderer="../templates/mlva_analysis_phylogenetics.jinja2")
#def phlMLVA_view(request):
#    process_ID = request.matchdict['ID']
#    query = request.db2_session.query(models.RepeatNumber).filter(
#        models.RepeatNumber.ID == process_ID).first()
#    if query is None:
#        raise HTTPNotFound()
#    return  {'RepeatNumber' :query }
#
#
#

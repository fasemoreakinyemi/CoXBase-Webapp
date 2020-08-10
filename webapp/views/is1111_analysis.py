from pyramid.view import view_config
from sqlalchemy.sql import insert
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPNotAcceptable
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


@view_config(route_name="is1111result")
def is1111process_view(request):
    VP = views_processor.ViewProcessor()
    if "fastafile" not in request.POST or "fastaentry" not in request.POST:
        raise HTTPNotFound()
    filename = ""
    process_ID = uuid.uuid4().hex
    try:
        filename = request.POST["fastafile"].filename
    except:
        pass
    if filename is not "":
        inputfile = request.POST["fastafile"].file
        file_path = VP.create_file_from_fastafile(inputfile, process_ID)
    else:
        sequence = memoryview(request.POST["fastaentry"].encode("utf-8"))
        file_path = VP.create_file_from_fastaentry(sequence, process_ID)
    command = VP.create_epcr_command_is1111(file_path, process_ID)
    subprocess.call(command)
    try:
        is1111_dict = VP.extract_is1111_values(process_ID)
    except:
        raise HTTPNotAcceptable()
    submission_dict = {
        "ID": process_ID,
        "AnalysisType": "is1111 Insilico typing",
        "IPaddress": request.remote_addr,
    }
    session = request.db2_session
    session.execute(insert(models.SubmissionTable).values([submission_dict]))
    session.execute(insert(models.is1111Profile).values([is1111_dict]))
    session.commit()
    url = request.route_url("resis1111", ID=process_ID)
    return HTTPFound(location=url)


@view_config(
    route_name="resis1111", renderer="../templates/is1111_analysis_result_table.jinja2"
)
def resis1111_view(request):
    process_ID = request.matchdict["ID"]
    query1 = (
        request.db2_session.query(models.is1111Profile)
        .filter(models.is1111Profile.ID == process_ID)
        .first()
    )
    if query1 is None:
        raise HTTPNotFound()
    return {"result": query1}


@view_config(
    route_name="resis1111", request_method="POST", renderer="json"
)
def resis1111_view_post(request):
    process_ID = request.matchdict["ID"]
    query1 = (
        request.db2_session.query(models.is1111Profile)
        .filter(models.is1111Profile.ID == process_ID)
        .first()
    )

    if query1 is None:
        raise HTTPNotFound()
    wanted = query1.__dict__
    wanted.pop('_sa_instance_state', None)
    return wanted


#
# @view_config(route_name='subMLVA',
#             renderer="../templates/mlva_analysis_submission_table.jinja2")
# def subMLVA_view(request):
#    process_ID = request.matchdict['ID']
#    query = request.db2_session.query(models.SubmissionTable).filter(
#        models.SubmissionTable.ID == process_ID).first()
#    if query is None:
#        raise HTTPNotFound()
#    return  {'submission' :query }
#
#
#
# @view_config(route_name='phlMLVA',
#             renderer="../templates/mlva_analysis_phylogenetics.jinja2")
# def phlMLVA_view(request):
#    process_ID = request.matchdict['ID']
#    query = request.db2_session.query(models.RepeatNumber).filter(
#        models.RepeatNumber.ID == process_ID).first()
#    if query is None:
#        raise HTTPNotFound()
#    return  {'RepeatNumber' :query }

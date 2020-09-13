from pyramid.view import view_config
from sqlalchemy.sql import insert
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPNotAcceptable
from pyramid.httpexceptions import HTTPBadRequest
from pathlib2 import Path
from webapp import models
import pandas as pd
import subprocess
import os
import uuid
import shutil
import json
import pyfastcopy
from Bio import pairwise2, SeqIO
from webapp import views_processor


@view_config(route_name="SNPHresult")
def processHornstra_view(request):
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
        file_path = VP.create_file_from_fastafile(inputfile, process_ID, "sole")
    else:
        sequence = memoryview(request.POST["fastaentry"].encode("utf-8"))
        file_path = VP.create_file_from_fastaentry(sequence, process_ID)
    try:
        typing_dict = VP.snpHornstraprocessor(file_path, process_ID)
    except:
        raise HTTPNotAcceptable()
    submission_dict = {
        "ID": process_ID,
        "AnalysisType": "Hornstra Insilico typing",
        "IPaddress": request.remote_addr,
    }
    session = request.db2_session
    session.execute(insert(models.SubmissionTable).values([submission_dict]))
    session.execute(insert(models.snpHornstra).values([typing_dict]))
    session.commit()
    url = request.route_url("resHornstra", ID=process_ID)
    return HTTPFound(location=url)


@view_config(
    route_name="resHornstra", renderer="../templates/hornstra_analysis_result_table.jinja2"
)
def resHornstra_view(request):
    process_ID = request.matchdict["ID"]
    try:
        query = (
            request.db2_session.query(models.snpHornstra)
            .filter(models.snpHornstra.ID == process_ID)
            .first()
        )
    except:
        raise HTTPNotFound()
    if query is None:
        raise HTTPNotFound()
    return {"result": query}



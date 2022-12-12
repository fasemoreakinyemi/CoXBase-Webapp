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


@view_config(route_name="adaresult")
def adaAprocess_view(request):
    process_ID = uuid.uuid4().hex
    VP = views_processor.ViewProcessor()
    if "fastafile" in request.POST:
        inputfile = request.POST["fastafile"].file
        file_path = VP.create_file_from_fastafile(inputfile, process_ID, "sole")
    else:
        if "fastaentry" in request.POST:
            sequence = memoryview(request.POST["fastaentry"].encode("utf-8"))
            file_path = VP.create_file_from_fastaentry(sequence, process_ID)
        else:
            raise HTTPNotFound()
    typing_dict = VP.adaprocessor(file_path, process_ID, "sole")
    submission_dict = {
        "ID": process_ID,
        "AnalysisType": "adaA Insilico typing",
        "IPaddress": request.remote_addr,
    }
    session = request.db2_session
    session.execute(insert(models.SubmissionTable).values([submission_dict]))
    session.execute(insert(models.adaAProfile).values([typing_dict]))
    session.commit()
    url = request.route_url("resadaA", ID=process_ID)
    return HTTPFound(location=url)


@view_config(
    route_name="resadaA", renderer="../templates/adaA_analysis_result_table.jinja2"
)
def resadaA_view(request):
    process_ID = request.matchdict["ID"]
    try:
        query = (
            request.db2_session.query(models.adaAProfile)
            .filter(models.adaAProfile.ID == process_ID)
            .first()
        )
    except:
        raise HTTPNotFound()
    if query is None:
        raise HTTPNotFound()
    return {"result": query}




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
from webapp import views_processor


@view_config(route_name="mlvaresult")
def mlvaprocess_view(request):
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
    command = VP.create_epcr_command(file_path, process_ID, "sole", "mlva")
    subprocess.call(command)
    try:
        mlva_dict = VP.extract_mlva_values(process_ID, "sole")
    except:
        raise HTTPNotAcceptable()

    submission_dict = {
        "ID": process_ID,
        "AnalysisType": "mlva Insilico typing",
        "IPaddress": request.remote_addr,
    }
    session = request.db2_session
    session.execute(insert(models.SubmissionTable).values([submission_dict]))
    session.execute(insert(models.ProductLength).values([mlva_dict.get("product")]))
    session.execute(insert(models.RepeatSize).values([mlva_dict.get("repeatSize")]))
    session.execute(insert(models.RepeatNumber).values([mlva_dict.get("repeat")]))
    session.execute(insert(models.FlankLength).values([mlva_dict.get("flank")]))
    session.commit()
    url = request.route_url("resMLVA", ID=process_ID)
    return HTTPFound(location=url)


@view_config(
    route_name="resMLVA", renderer="../templates/mlva_analysis_result_table.jinja2"
)
def resMLVA_view(request):
    process_ID = request.matchdict["ID"]
    try:
        query1 = (
            request.db2_session.query(models.ProductLength)
            .filter(models.ProductLength.ID == process_ID)
            .first()
        )
    except:
        raise HTTPNotFound()
    if query1 is None:
        raise HTTPNotFound()
    query2 = (
        request.db2_session.query(models.FlankLength)
        .filter(models.FlankLength.ID == process_ID)
        .first()
    )
    query3 = (
        request.db2_session.query(models.RepeatSize)
        .filter(models.RepeatSize.ID == process_ID)
        .first()
    )
    query4 = (
        request.db2_session.query(models.RepeatNumber)
        .filter(models.RepeatNumber.ID == process_ID)
        .first()
    )
    return {
        "ProductLength": query1,
        "FlankLength": query2,
        "RepeatSize": query3,
        "RepeatNumber": query4,
    }


@view_config(
    route_name="subMLVA", renderer="../templates/mlva_analysis_submission_table.jinja2"
)
def subMLVA_view(request):
    process_ID = request.matchdict["ID"]
    try:
        query = (
            request.db2_session.query(models.SubmissionTable)
            .filter(models.SubmissionTable.ID == process_ID)
            .first()
        )
    except:
        raise HTTPNotFound()
    if query is None:
        raise HTTPNotFound()
    return {"submission": query}


@view_config(
    route_name="phlMLVA", renderer="../templates/mlva_analysis_phylogenetics.jinja2"
)
def phlMLVA_view(request):
    process_ID = request.matchdict["ID"]
    query = (
        request.db2_session.query(models.RepeatNumber)
        .filter(models.RepeatNumber.ID == process_ID)
        .first()
    )
    if query is None:
        raise HTTPNotFound()
    return {"RepeatNumber": query}

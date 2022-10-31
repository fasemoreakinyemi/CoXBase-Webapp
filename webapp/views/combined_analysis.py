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


@view_config(route_name="combinedresult")
def combined_result_view(request):
    VP = views_processor.ViewProcessor()
    session = request.db2_session
    process_ID = uuid.uuid4().hex
    if "fastafile" in request.POST:
        inputfile = request.POST["fastafile"].file
        file_path = VP.create_file_from_fastafile(inputfile,
                                                  process_ID,
                                                  "combined")
    else:
        if "fastaentry" in request.POST:
            sequence = memoryview(request.POST["fastaentry"].encode("utf-8"))
            file_path = VP.create_file_from_fastaentry(sequence, process_ID)
        else:
            raise HTTPNotFound()


    # mlva
    command = VP.create_epcr_command(file_path, process_ID,"combined", "mlva")
    subprocess.call(command)
    try:
        mlva_dict = VP.extract_mlva_values(process_ID, "combined")
    except:
        raise HTTPNotAcceptable()
    session.execute(insert(models.ProductLength).values([mlva_dict.get("product")]))
    session.execute(insert(models.RepeatSize).values([mlva_dict.get("repeatSize")]))
    session.execute(insert(models.RepeatNumber).values([mlva_dict.get("repeat")]))
    session.execute(insert(models.FlankLength).values([mlva_dict.get("flank")]))

    # mst
    try:
        spacer_dict = VP.mstprocessor(file_path, process_ID, "combined")
    except:
        raise HTTPNotAcceptable()

    session.execute(insert(models.mstSpacerResult).values([spacer_dict]))

    # is1111
    command = VP.create_epcr_command(file_path, process_ID, "combined", "is1111")
    subprocess.call(command)
    try:
        is1111_dict = VP.extract_is1111_values(process_ID, "combined")
    except:
        raise HTTPNotAcceptable()
    session.execute(insert(models.is1111Profile).values([is1111_dict]))

    # ada
    typing_dict = VP.adaprocessor(file_path, process_ID, "combined")
    session.execute(insert(models.adaAProfile).values([typing_dict]))
    
    # SNP Hornstra
    typing_dict = VP.snpHornstraprocessor(file_path, process_ID)
    session.execute(insert(models.snpHornstra).values([typing_dict]))

    # submission dict
    submission_dict = {
        "ID": process_ID,
        "AnalysisType": "comp Insilico typing",
        "IPaddress": request.remote_addr,
    }
    session.execute(insert(models.SubmissionTable).values([submission_dict]))

    session.commit()
    VP.delete_temp_files(process_ID, "combined")
    url = request.route_url("resCombined", ID=process_ID)
    return HTTPFound(location=url)


@view_config(
    route_name="resCombined",
    renderer="../templates/combined_analysis_result_table.jinja2",
)
def resCombined_view(request):
    process_ID = request.matchdict["ID"]
    return {"ID": process_ID}



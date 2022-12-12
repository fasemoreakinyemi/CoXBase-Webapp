
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


@view_config(route_name="multi_marker", renderer="../templates/multimarker.jinja2")
def multimaker_view(request):
    return {}


@view_config(route_name="multi_marker_result", renderer="json")
def multimaker_analysis_view(request):
    VP = views_processor.ViewProcessor()
    process_ID = uuid.uuid4().hex
    mlva_markers = json.loads(request.POST["mlva_markers"])
    mst_markers = json.loads(request.POST["mst_spacers"])
    inputfile = request.POST["fastafile"].file
    file_path = VP.create_file_from_fastafile(inputfile, process_ID, "sole")
    if mlva_markers != []:
        command = VP.create_epcr_command(file_path, process_ID, "sole", "mlva")
        subprocess.call(command)
        try:
            mlva_dict = VP.extract_mlva_values(process_ID, "sole", mlva_markers)["repeat"]
        except:
            raise HTTPNotAcceptable()
    if mst_markers != []:
        try:
            spacer_dict = VP.mstprocessor(file_path, process_ID, "sole", mst_markers)
        except:
            raise HTTPNotAcceptable()
    if mlva_markers != [] and mst_markers != []:
        del spacer_dict["ID"]
        print(spacer_dict)
        result_dict = {**mlva_dict, **spacer_dict}
        return {"result": result_dict}
    else:
        if mlva_markers != []:
            return {"result": mlva_dict}
        else:
            return {"result": spacer_dict}

#
#    submission_dict = {
#        "ID": process_ID,
#        "AnalysisType": "mlva Insilico typing",
#        "IPaddress": request.remote_addr,
#    }
#    session = request.db2_session
#    session.execute(insert(models.SubmissionTable).values([submission_dict]))
#    session.execute(insert(models.ProductLength).values([mlva_dict.get("product")]))
#    session.execute(insert(models.RepeatSize).values([mlva_dict.get("repeatSize")]))
#    session.execute(insert(models.RepeatNumber).values([mlva_dict.get("repeat")]))
#    session.execute(insert(models.FlankLength).values([mlva_dict.get("flank")]))
#    session.commit()
#    url = request.route_url("resMLVA", ID=process_ID)
#HTTPFound(location=url)


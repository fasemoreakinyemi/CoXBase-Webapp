#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config
from pyramid_mailer.message import Message
from sqlalchemy.sql import insert
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPNotAcceptable
from sqlalchemy.exc import DBAPIError
import uuid
from .. import models
import pandas as pd
from io import StringIO


@view_config(route_name="usersubmission", renderer="../templates/submissions_landing.jinja2")
def usersubmission_view(request):
    return {}

@view_config(route_name="s_submission", renderer="../templates/submissions.jinja2")
def ssubmission_view(request):
    return {}

@view_config(route_name="b_submission", renderer="../templates/submissions_bulk.jinja2")
def bsubmission_view(request):
    return {}


@view_config(route_name="subForm")
def usersubmission_form(request):
    mailer = request.mailer
    submissionID = uuid.uuid4().hex
    properties_dict = {"ID": submissionID}
    markers_dict = {"ID": submissionID, "isolateID": submissionID}
    session = request.db2_session
    properties_list = [
        "submissionType",
        "isolateName",
        "isolateSource",
        "isolateHost",
        "placeOfIsolation",
        "yearOfIsolation",
        "country",
        "longitude",
        "latitude",
        "pubmedID",
        "genomeAccession",
        "email",
        "submitterName",
    ]

    if not request.POST["submissionType"]:
        return HTTPNotFound()
    for item in properties_list:
        properties_dict[item] = request.POST.get(item)
    session.execute(insert(models.isolateSubmission).values([properties_dict]))

    if request.POST["submissionType"] == "mlva":
        markers_list = [
            "ms01",
            "ms03",
            "ms20",
            "ms21",
            "ms22",
            "ms23",
            "ms24",
            "ms26",
            "ms27",
            "ms28",
            "ms30",
            "ms31",
            "ms33",
            "ms34"
        ]
        for item in markers_list:
            if request.POST.get(item):
                markers_dict[item] = request.POST.get(item)
        session.execute(insert(models.mlvaSubmission).values([markers_dict]))
    else:
        markers_list = [
            "cox2",
            "cox5",
            "cox18",
            "cox20",
            "cox22",
            "cox37",
            "cox51",
            "cox56",
            "cox57",
            "cox61"
        ]
        for item in markers_list:
            markers_dict[item] = request.POST.get(item)
        session.execute(insert(models.mstSubmission).values([markers_dict]))

    session.commit()
    #  body = "test again {}".format(submissionID)
    body = """Dear {},\n
    Your submision with ID {}, has been submitted to CoxBase for curation.\n
    You can preview it with the below link.\n
    https://coxbase.q-gaps.de/webapp/submissions/form/preview/{}\n
    Regards,\n
    CoxBase Curator""".format(
        request.POST.get("submitterName"), submissionID, submissionID
    )
    message = Message(
        subject="Submission on CoxBase",
        sender="admin@coxiella.net",
        recipients=[request.POST.get("email"), "fasemoremandela@gmail.com"],
        body=body,
    )
    try:
        mailer.send(message)
    except:
        raise HTTPNotAcceptable()

    url = request.route_url("subFormPrev", ID=submissionID)
    return HTTPFound(location=url)


@view_config(route_name="subBulkForm")
def bulksubmission_form(request):
    mailer = request.mailer
    isolateID = uuid.uuid4().hex
    session = request.db2_session
    sent_data = StringIO(request.POST["datafield"])
    df = pd.read_csv(sent_data, sep="\t")
    df_dict = df.to_dict('records')
    properties_list = [
        "isolateName",
        "isolateSource",
        "isolateHost",
        "placeOfIsolation",
        "yearOfIsolation",
        "country",
        "pubmedID",
        "email",
        "submitterName",
    ]

    if not request.POST["submissionType"]:
        return HTTPNotFound()
    for entries in df_dict:
        entries_id = uuid.uuid4().hex
        properties_dict = dict([(key, entries[key]) for key in properties_list])
        properties_dict["ID"] = entries_id
        properties_dict["submissionType"] = request.POST["submissionType"]
        session.execute(insert(models.isolateSubmission).values([properties_dict]))
        if request.POST["submissionType"] == "mlva":
            markers_list = ["ms01", "ms03", "ms20", "ms21",
                            "ms22", "ms23", "ms24", "ms26",
                            "ms27", "ms28", "ms30", "ms31",
                            "ms33", "ms34"]
            markers_dict = dict([(key, entries[key]) for key in markers_list])
            markers_dict["ID"] = entries_id
            markers_dict["isolateID"] = entries_id
            session.execute(insert(models.mlvaSubmission).values([markers_dict]))
        else:
            markers_list = ["cox2", "cox5", "cox18", "cox20",
                            "cox22", "cox37", "cox51", "cox56",
                            "cox57", "cox61"]
            markers_dict = dict([(key, entries[key]) for key in markers_list])
            markers_dict["ID"] = entries_id
            markers_dict["isolateID"] = entries_id
            session.execute(insert(models.mstSubmission).values([markers_dict]))

    session.commit()
    #  body = "test again {}".format(submissionID)
    body = """Dear {},\n
    Your submision has been submitted to CoxBase for curation.\n
    You can preview it with the below link.\n
    https://coxbase.q-gaps.de/webapp/submissions/form/preview/\n
    Regards,\n
    CoxBase Curator""".format(
        request.POST.get("submitterName"))
    message = Message(
        subject="Submission on CoxBase",
        sender="admin@coxbase.qgaps.de",
        recipients=[request.POST.get("email"), "fasemoremandela@gmail.com"],
        body=body,
    )
    try:
        mailer.send(message)
    except:
        raise HTTPNotAcceptable()

    url = request.route_url("b_submission")
    return HTTPFound(location=url)
@view_config(
    route_name="subFormPrev", renderer="../templates/submissionsPreview.jinja2"
)
def usersubmission_prev(request):
    ID = request.matchdict["ID"]
    query = (
        request.db2_session.query(models.isolateSubmission)
        .filter(models.isolateSubmission.ID == ID)
        .first()
    )
    queryMLVA = (
        request.db2_session.query(models.mlvaSubmission)
        .filter(models.isolateSubmission.ID == ID)
        .first()
    )
    queryMST = (
        request.db2_session.query(models.mstSubmission)
        .filter(models.isolateSubmission.ID == ID)
        .first()
    )
    if query is None:
        raise HTTPNotFound()
    if query and queryMLVA:
        return {"submission": query, "mlva": queryMLVA}
    return {"submission": query, "mst": queryMST}

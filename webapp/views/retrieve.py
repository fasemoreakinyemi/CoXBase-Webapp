#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config
from pyramid_mailer.message import Message
from sqlalchemy.sql import insert
from pyramid.response import Response
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )
from sqlalchemy.exc import DBAPIError
import uuid
from .. import models

@view_config(route_name='retrieve_submission', renderer='../templates/retrieve_submissions.jinja2')
def retrieve_view(request):
    if 'submit' in request.params:
        process_ID = request.params['submissionID']
        query = request.db2_session.query(models.SubmissionTable).filter(models.SubmissionTable.ID == process_ID).first()
        if query:
            analysisType = query.AnalysisType.split(" ")[0]
            resultsLink = "location.href='result/{}/{}'".format(analysisType,process_ID)
            return  {"style": "display:block;","submission" :query ,"submissionID":process_ID, "resultlink": resultsLink}
        return {"message": "Invalid submission ID", "submissionID":process_ID,"style": "display:None;"}
    return {"style": "display:None;"}

#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base
from .. import process_request
from sqlalchemy import or_
from .. import models
import logging
import traceback
from webapp import process_request
import sys
from webapp import automapper
import os

head_path = os.path.dirname(__file__).split("webapp/views")[0]
config_path = os.path.join(head_path, 'development.ini')
am = automapper.Automapper(config_path)
base_automap = am.generate_base("db2.")


@view_config(
    route_name="entry_view_mlva", renderer="../templates/mlva_query_view.jinja2"
)
def detailed_mlva_view(request):
    ID = request.matchdict["ID"]
    isolates = getattr(base_automap, "isolates2022")
    try:
        query = request.db2_session.query(isolates).filter(isolates.mlvaGenotype == ID)
        # query = request.db2_session.query(isolates).join(isolatesRef, isolates.isolateid == isolatesRef.isolate_id).filter(isolatesRef.pmid  == 25037926).filter(
        #    isolates.mlvaGenotype == ID)
    except DBAPIError:
        return Response(db_err_msg, content_type="text/plain", status=500)
    return {"count": query.count(), "results": query.all()}

@view_config(
    route_name="entry_view_mlva_6", renderer="../templates/mlva_tilburg_query_view.jinja2"
)
def detailed_mlva_tilburg_view(request):
    ID = request.matchdict["ID"]
    isolates = getattr(base_automap, "isolates2022")
    try:
        query = request.db2_session.query(isolates).filter(isolates.mlvaGenotype == ID)
    except DBAPIError:
        return Response(db_err_msg, content_type="text/plain", status=500)
    return {"count": query.count(), "results": query.all()}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from .. import process_request
from sqlalchemy import or_
from sqlalchemy import func, case
from sqlalchemy import desc
from .. import models
import logging
import traceback
import sys

Base = automap_base()
settings = get_appsettings(
    "/home/ubuntu/coxbase/coxbase/webapp/development.ini", name="main"
)
engine = engine_from_config(settings, "db2.")
Base.prepare(engine, reflect=True)

def distance_query(spacer_list, request, distance):
    case_list = []
    mstgroups = Base.classes.mstgroups2
    for spacers in spacer_list:
        if int(request.matchdict[spacers]) == 0:
            continue
        else:
            spacer_model = getattr(mstgroups, spacers)
            spacer_case = case([
                (spacer_model == int(request.matchdict[spacers]), 1)], else_=0
            )
            case_list.append(spacer_case)
    try:
        query = (
            request.db2_session.query(mstgroups).filter(sum(case_list) >= distance)
            .order_by(desc(sum(case_list))).all()
        )
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        inf = "".join("!!" + line for line in lines)
        return {"line": inf}
    return query


@view_config(route_name="mstquery", renderer="../templates/mst_query.jinja2")
def mst_view(request):
    return {}


@view_config(route_name="mst_query_api", renderer="json")
def mstq_view(request):
    RP = process_request.RequestProcessor()
    mstgroups = Base.classes.mstgroups2
    spacer_list = [
        "COX2",
        "COX5",
        "COX18",
        "COX20",
        "COX22",
        "COX37",
        "COX51",
        "COX56",
        "COX57",
        "COX61",
    ]
    distance = {"0":10, "1":9, "2":8, "3":7, "4":6, "5":5, "xx":1}[request.matchdict["distance"]]
    query = distance_query(spacer_list, request, distance)
    return RP._serialize_mst(query)  # {len(conditionOr):len(conditionAnd)}


@view_config(route_name="entry_view_mst", renderer="../templates/mst_view.jinja2")
def detailed_mst_view(request):
    ID = request.matchdict["ID"]
    isolates = Base.classes.isolates2022
    isolatesRef = Base.classes.isolate_pub_ref
    try:
        query = request.db2_session.query(isolates).filter(isolates.mstGroup == ID)
    except DBAPIError:
        return Response(db_err_msg, content_type="text/plain", status=500)
    return {"count": query.count(), "results": query.all()}

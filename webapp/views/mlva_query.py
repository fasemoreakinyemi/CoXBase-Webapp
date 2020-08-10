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
from sqlalchemy import or_, between
from .. import models
import logging
import traceback
import sys


@view_config(route_name="mlvaquery", renderer="../templates/mlva_query.jinja2")
def mlva_view(request):
    return {}


@view_config(route_name="fp_query_api", renderer="json")
def fpq_view(request):
    RP = process_request.RequestProcessor()
    repeat_list = [
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
        "ms34",
    ]
    conditionAnd = []
    conditionOr = []
    Base = automap_base()
    settings = get_appsettings(
        "/home/ubuntu/coxbase/coxbase/webapp/development.ini", name="main"
    )
    engine = engine_from_config(settings, "db2.")
    Base.prepare(engine, reflect=True)
    mlvaTable = Base.classes.mlva_normalized
    for repeats in repeat_list:
        if float(request.matchdict[repeats]) == 0:
            continue
        else:
            repeat_model = getattr(mlvaTable, repeats)
            repeat_query = (
                request.db2_session.query(mlvaTable)
                .filter(repeat_model == float(request.matchdict[repeats]))
                .first()
            )
            if repeat_query:
                conditionAnd.append(repeat_model.between(float(int(request.matchdict[repeats])-1),
                                                         float(request.matchdict[repeats])))
                query = ( request.db2_session.query(mlvaTable).filter(*conditionAnd).first()
                )
                if query:
                    continue
                else:
                    conditionAnd.pop()
            else:
                repeat_query = (
                    request.db2_session.query(mlvaTable)
                    .filter(repeat_model == float(int(request.matchdict[repeats])-1))
                    .first()
                )
                if repeat_query:
                    conditionAnd.append(repeat_model == float(int(request.matchdict[repeats])-1))
                    query = (
                        request.db2_session.query(mlvaTable).filter(*conditionAnd).first()
                    )
                    if query:
                        continue
                    else:
                        conditionAnd.pop()

    if conditionAnd == []:
        return {"STATUS": "NO MATCH"}
    try:
        query = (
            request.db2_session.query(mlvaTable).filter(*conditionAnd).all()
        )  # (or_(*conditionOr)).all()#filter(*conditionAnd).all()

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        inf = "".join("!!" + line for line in lines)
        return {"line": inf}

    # while conditionAnd:
    #     if conditionAnd and query:
    #         break
    #     else:
    #         conditionAnd.pop()
    #         query = request.db2_session.query(mlvaTable).all()
    #        # query = request.db2_session.query(mlva).filter(*conditionAnd).all()
    return RP._serialize_mlva(query)  # {len(conditionOr):len(conditionAnd)}

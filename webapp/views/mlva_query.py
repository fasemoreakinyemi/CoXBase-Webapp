#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

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
from webapp import automapper
from sqlalchemy import func, case
from sqlalchemy import desc


am = automapper.Automapper("/home/travis/build/foerstner-lab/CoxBase-Webapp/development.ini")
Base_automap = am.generate_base("db2.")

def distance_query(Base, repeat_list, request, distance, db):
    case_list = []
    mlvaTable = getattr(Base, db) #Base.classes.mlva_normalized
    for repeats in repeat_list:
        if float(request.matchdict[repeats]) == 0:
            continue
        else:
            repeat_model = getattr(mlvaTable, repeats)
            repeat_case = case([
                (repeat_model == float(request.matchdict[repeats]), 1)], else_=0
            )
            case_list.append(repeat_case)

    try:
        query = (
            request.db2_session.query(mlvaTable).filter(sum(case_list) >= distance)
            .order_by(desc(sum(case_list))).all()
        )

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        inf = "".join("!!" + line for line in lines)
        return {"line": inf}
    return query




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
    distance = {"0":14, "1":13, "2":12, "3":11, "4":10, "5":9, "xx":1}[request.matchdict["distance"]]
    query = distance_query(Base_automap,
                           repeat_list,
                           request,
                           distance,
                           "mlva_normalized") 
    return RP._serialize_mlva(query)

@view_config(route_name="tp_query_api", renderer="json")
def tpq_view(request):
    RP = process_request.RequestProcessor()
    repeat_list = [
        "ms23",
        "ms24",
        "ms27",
        "ms28",
        "ms33",
        "ms34",
    ]
    distance = {"0":6, "1":5, "2":4, "3":3, "4":2, "5":1, "xx":0}[request.matchdict["distance"]]
    query = distance_query(Base_automap,
                           repeat_list,
                           request,
                           distance,
                           "tilburg_profile2022") 

    return RP._serialize_mlva_tillburg(query)



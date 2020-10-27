#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.sql import text
from sqlalchemy.ext.automap import automap_base
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from .. import process_request
from sqlalchemy import or_
from .. import models
import logging
import traceback
import sys

Base = automap_base()
settings = get_appsettings(
    "/home/travis/build/foerstner-lab/CoxBase-Webapp/development.ini", name="main"
)
engine = engine_from_config(settings, "db2.")
Base.prepare(engine, reflect=True)


@view_config(route_name="primerquery", renderer="../templates/primer_query.jinja2")
def primer_view(request):
    return {}


@view_config(
    route_name="primerquery_results",
    renderer="../templates/primer_query_results.jinja2",
)
def primer_results_view(request):
    primers = Base.classes.primer
    is_query = text("primers.name like 'IS%'")
    query_dict = {
        "mlva": primers.name.like("ms__\_%"),
        "mst": primers.name.like("mst%"),
        "is": text("primer.name like 'is%' and primer.pmid is not null"),
        "snp": primers.name.like("ada%"),
        "plasmid": primers.name.like("Q%"),
    }
    condition_list = []
    wanted_seq = request.matchdict["selection"]
    if len(wanted_seq) == 1:
        try:
            query = (
                request.db2_session.query(primers)
                .filter(query_dict.get(wanted_seq[0]))
                .filter(primers.pmid > 0)
            )
        except DBAPIError:
            return Response(db_err_msg, content_type="text/plain", status=500)
        return {"count": query.count(), "results": query.all()}
    else:
        for items in wanted_seq:
            condition_list.append(query_dict.get(items, None))
        try:
            query = (
                request.db2_session.query(primers)
                .filter(or_(*condition_list))
                .filter(primers.pmid > 0)
            )
        except DBAPIError:
            return Response(db_err_msg, content_type="text/plain", status=500)
        return {"count": query.count(), "results": query.all()}

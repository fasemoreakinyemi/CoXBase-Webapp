#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config
from pyramid.paster import get_appsettings
from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import or_
from sqlalchemy import and_
import json
from .. import process_request
from .. import newick_generator
import uuid
from .. import models

Base = automap_base()
settings = get_appsettings(
    "/home/ubuntu/coxbase/coxbase/webapp/development.ini", name="main"
)
engine = engine_from_config(settings, "db2.")
Base.prepare(engine, reflect=True)
RP = process_request.RequestProcessor()
NG = newick_generator.NewickProcessor()


@view_config(route_name="phyd3_tree", renderer="../templates/phyd3_tree_plot.jinja2")
def phyd3_tree_view(request):
    process_ID = request.matchdict["ID"]
    try:
        nwk = (
            request.db2_session.query(models.NewickTable.nwk)
            .filter(models.NewickTable.ID == process_ID)
            .first()
        )
    except:
        raise HTTPNotFound()
    return {}



@view_config(route_name="phyd3_tree_api", renderer="json")
def phyd3_tree_api_view(request):
    process_ID = request.matchdict["ID"]
    try:
        nwk = (
            request.db2_session.query(models.NewickTable.nwk)
            .filter(models.NewickTable.ID == process_ID)
            .first()
        )
    except:
        return {"staus": "not found"}
    return {"itms": "{}".format(process_ID), "nwk": str(nwk)}

#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import or_
import json
from .. import process_request

Base = automap_base()
settings = get_appsettings("/home/ubuntu/coxbase/coxbase/webapp/development.ini", name="main")
engine = engine_from_config(settings, 'db2.')
Base.prepare(engine, reflect=True)

@view_config(route_name='isolate_query', renderer='../templates/isolate_query.jinja2')
def isolate_query_view(request):
    return {}

@view_config(route_name='isolate_query_api',renderer='json')
def isolate_query_api_view(request):
    RP = process_request.RequestProcessor()
    container = request.matchdict["cont"]
    combo = request.matchdict["combo"]
    query_container = json.loads(container)
    
    isolates_table = Base.classes.isolates
    isolatesRef = Base.classes.isolate_refs2
    
    conditionAnd = []
    conditionOr = []
    subject_dict = {"year":"yearOfIsolation",
                   "host":"host",
                   "country":"country",
                   "plasmid":"plasmidType",
                   "MST group": "mstGroup",
                   "MLVA Genotype": "mlvaGenotype"}
    
    for items in query_container:
        subject = subject_dict[items[0]]
        models = getattr(isolates_table, subject)
        operatr = items[1]
        value = items[2]

        if operatr == "=":
            query = request.db2_session.query(isolates_table).filter(
                models == value).first()
            if query:
                if combo == "AND":
                    conditionAnd.append(models==value)
                else:
                    conditionOr.append(models==value)
        elif operatr == "contains":
            query = request.db2_session.query(isolates_table).filter(
                models.like("%{}%".format(value))).first()
            if query:
                if combo == "AND":
                    conditionAnd.append(models.like("%{}%".format(value)))
                else:
                    conditionOr.append(models.like("%{}%".format(value)))
        elif operatr == "starts with":
            query = request.db2_session.query(isolates_table).filter(
                models.like("{}%".format(value))).first()
            if query:
                if combo == "AND":
                    conditionAnd.append(models.like("{}%".format(value)))
                else:
                    conditionOr.append(models.like("{}%".format(value)))
        elif operatr == "ends with":
            query = request.db2_session.query(isolates_table).filter(
                models.like("%{}".format(value))).first()
            if query:
                if combo == "AND":
                    conditionAnd.append(models.like("%{}".format(value)))
                else:
                    conditionOr.append(models.like("%{}".format(value)))
        else:
            query = request.db2_session.query(isolates_table).filter(
                models != value).first()
            if query:
                if combo == "AND":
                    conditionAnd.append(models!=value)
                else:
                    conditionOr.append(models!=value)
    if combo == "AND":
        final_query = request.db2_session.query(isolates_table).filter(*conditionAnd).all()
    else:
        final_query = request.db2_session.query(isolates_table).filter(or_(*conditionOr)).all()
    if final_query:
        return  RP._serialize_ctr_dts(final_query)
    return {"STATUS": "None"}

#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import or_
from sqlalchemy import and_
import json
from .. import process_request

Base = automap_base()
settings = get_appsettings("/home/ubuntu/coxbase/coxbase/webapp/development.ini", name="main")
engine = engine_from_config(settings, 'db2.')
Base.prepare(engine, reflect=True)
RP = process_request.RequestProcessor()

@view_config(route_name='isolate_query', renderer='../templates/isolate_query.jinja2')
def isolate_query_view(request):
    return {}

@view_config(route_name='isolate_query_api',renderer='json')
def isolate_query_api_view(request):
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
                   "mst": "mstGroup",
                   "ada": "adaGene",
                   "mlva": "mlvaGenotype"}
    
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
        elif operatr == "starts":
            query = request.db2_session.query(isolates_table).filter(
                models.like("{}%".format(value))).first()
            if query:
                if combo == "AND":
                    conditionAnd.append(models.like("{}%".format(value)))
                else:
                    conditionOr.append(models.like("{}%".format(value)))
        elif operatr == "ends":
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
        if conditionAnd == []:
            return {"STATUS": "None"}
        else:
            final_query = request.db2_session.query(isolates_table).filter(and_(*conditionAnd)).all()
    else:
        if conditionOr == []:
            return {"STATUS": "None"}
        else:
            final_query = request.db2_session.query(isolates_table).filter(or_(*conditionOr)).all()
    return  RP._serialize_ctr_dts_iso(final_query)

@view_config(route_name='isolate_query_fc', renderer='../templates/isolate_query_faceted.jinja2')
def isolate_query_fc_view(request):
    return {}

@view_config(route_name='isolate_fc_api', renderer='json')
def get_all_isolates(request):
    isolates = Base.classes.isolates
    isolatesRef = Base.classes.isolate_refs2
    query = request.db2_session.query(isolates).all()
  #  query = request.db2_session.query(isolates).filter(isolates.country == country_id).all()
    return RP._serialize_ctr_dts_ls(query)

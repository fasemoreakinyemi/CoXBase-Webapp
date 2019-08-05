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
import  sys

Base = automap_base()
settings = get_appsettings("/home/ubuntu/coxbase/coxbase/webapp/development.ini", name="main")
engine = engine_from_config(settings, 'db2.')
Base.prepare(engine, reflect=True)

@view_config(route_name='mlvaanalysis', renderer='../templates/mlvaanalysis.jinja2')
def mlvaanalysis_view(request):
    return {}


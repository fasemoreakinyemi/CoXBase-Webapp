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


@view_config(route_name='mlvaanalysis', renderer='../templates/mlva_analysis.jinja2')
def mlvaanalysis_view(request):
    return {}

@view_config(route_name='mstanalysis', renderer='../templates/mst_analysis.jinja2')
def mstanalysis_view(request):
    return {}

@view_config(route_name='is1111analysis', renderer='../templates/is1111_analysis.jinja2')
def is1111alysis_view(request):
    return {}

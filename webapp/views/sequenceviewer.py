#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError


@view_config(route_name="sequenceviewer", renderer="../templates/sequenceviewer.jinja2")
def primer_view(request):
    return {}

#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from .. import process_request
from sqlalchemy import or_
from .. import models


@view_config(route_name='test', renderer='json')
def testapi_view(request):
    num = request.matchdict['num']
    return {num:"working"}

@view_config(route_name='hello_baby',
             request_method='GET',
             renderer='string')
def hello_baby(request):
    import logging
    logger = logging.getLogger('waitress')
    logger.info('Hello baby!')
    return 'Hi there'

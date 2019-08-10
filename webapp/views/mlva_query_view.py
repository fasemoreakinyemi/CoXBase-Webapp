#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

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

@view_config(route_name='detailed_view', renderer='../templates/mlva_query_view.jinja2')
def detailed_mlva_view(request):
    ID = request.matchdict['ID']
    try:
        query = request.db2_session.query(models.SampleMetadata).filter(
            models.SampleMetadata.MLVAID == ID)
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'count' : query.count(), 'results' : query.all()}

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

#@view_config(route_name='fp_query_api', renderer='json')
#def fpq_view(request):
#    RP = process_request.RequestProcessor()
#    repeat_list = ['ms01', 'ms03', 'ms20', 'ms21', 
#                 'ms22', 'ms23', 'ms24', 'ms26', 
#                 'ms27', 'ms28', 'ms30', 'ms31',
#                 'ms33', 'ms34']
#    conditionAnd = []
#    conditionOr = []
#
#    for repeats in repeat_list:
#        if float(request.matchdict[repeats]) == 0:
#            continue
#        else:
#            repeat_model = RP.get_repeat_model(repeats)
#            repeat_query = request.db2_session.query(models.mlvaProfile).filter(
#                repeat_model == float(request.matchdict[repeats])).first()
#            if repeat_query:
#                conditionAnd.append(repeat_model==float(request.matchdict[repeats]))
#            else:
#                conditionOr.append(repeat_model==float(request.matchdict[repeats]))
#    try:
#        query = request.db2_session.query(models.mlvaProfile).filter(*conditionAnd).all()#(or_(*conditionOr)).all()#filter(*conditionAnd).all()
#
#    except:
#        exc_type, exc_value, exc_traceback = sys.exc_info()
#        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
#        inf = ''.join('!!' + line for line in lines)
#        return {"line" : inf}
#    
#    while conditionAnd:
#        if conditionAnd and query:
#            break
#        else:
#            conditionAnd.pop()
#            query = request.db2_session.query(models.mlvaProfile).filter(*conditionAnd).all()
#    return RP._serialize_mlva(query)#{len(conditionOr):len(conditionAnd)}
#

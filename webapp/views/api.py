from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from .. import models
from .. import process_request



@view_config(route_name='api_column', renderer='json')
def api_filter(request):
    RP = process_request.RequestProcessor()
    _column = request.matchdict['column']
    model = RP.get_model(_column)
    if model:
        try:
            query = request.db2_session.query(model).all()
            result_dict = RP.to_dict(query)
        except DBAPIError:
            return RP.response_error()
        return result_dict
    else:
        return {'NOT': 'working'}



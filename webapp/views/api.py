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


@view_config(route_name='api_filter', renderer='json')
def model_filter(request):
    RP = process_request.RequestProcessor()
    _column = request.matchdict['column']
    model = RP.get_model(_column)
    _filter = request.matchdict['filter']
    filter_model = RP.get_model_filter(_filter)
    _filter_value = request.matchdict['filter_value']
    if model:
        try:
            query = request.db2_session.query(model).filter(filter_model == _filter_value).all()
            result_dict = RP.to_dict(query)
        except DBAPIError:
            return RP.response_error()
        return result_dict
    else:
        return {'NOT': 'working'}

@view_config(route_name='api_map', renderer='json')
def map_filter(request):
    RP = process_request.RequestProcessor()
    _column = request.matchdict['column']
    _filter_value = request.matchdict['state']
    query = request.db2_session.query(models.SampleMetadata)
    model = RP.get_model(_column)
    result = query.filter(model == _filter_value).all()
    return RP._serialize(result)

@view_config(route_name='api_view_map', renderer='json')
def get_coordinates(request):
    RP = process_request.RequestProcessor()
    _column = request.matchdict['ID']
    query = request.db2_session.query(models.SampleMetadata).filter(
        models.SampleMetadata.MLVAID == _column).all()
    return RP._serialize_coord(query)

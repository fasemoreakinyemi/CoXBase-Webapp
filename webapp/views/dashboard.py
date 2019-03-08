from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
import colander
from deform import Form
import deform.widget
from sqlalchemy.exc import DBAPIError
from .. import process_request

from .. import models

@view_config(route_name='dashboard', renderer='../templates/dashboard.jinja2')
def my_view(request):
    return {}

@view_config(route_name='dashboard_new', renderer='../templates/dashboard.jinja2')
def path_view(request):
    RP = process_request.RequestProcessor()
    model = RP.get_model('CountryProvince')
    if model:
        try:
            query = request.db2_session.query(model).all()
            result_dict = RP.to_dict(query)
        except DBAPIError:
            return RP.response_error()
        return {'Province' : result_dict.keys() }
    else:
        return {'Province' : 'two'}


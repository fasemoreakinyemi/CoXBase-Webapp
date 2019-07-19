from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
import colander
from deform import Form
import deform.widget
from sqlalchemy.exc import DBAPIError
#from .. import process_request

#from .. import models

@view_config(route_name='dashboard', renderer='../templates/dashboard.jinja2')
def my_view(request):
    return {}





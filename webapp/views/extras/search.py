from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
import colander
from deform import Form
import deform.widget
from sqlalchemy.exc import DBAPIError

from .. import models


@view_config(route_name="search", renderer="../templates/search_temp.jinja2")
def my_view(request):
    return {}

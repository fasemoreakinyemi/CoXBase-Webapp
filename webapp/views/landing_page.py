from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
import colander
from deform import Form
import deform.widget
from sqlalchemy.exc import DBAPIError


@view_config(route_name='home', renderer='../templates/landing_page.jinja2')
def my_view(request):
    if request.authenticated_userid:
        status = "Log out"
        route = 'logout'
        return {'status': status, 'route': route}
    return {'status': "Log in", 'route': 'login'}





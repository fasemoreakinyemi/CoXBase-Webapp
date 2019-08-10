from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='coxviewer', renderer='../templates/coxviewer.jinja2')
def my_view(request):
    return {}





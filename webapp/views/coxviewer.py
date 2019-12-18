from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='coxviewer', renderer='../templates/coxviewer.jinja2')
def coxmap_view(request):
    if request.authenticated_userid:
        status = "Log out"
        route = 'logout'
        return {'status': status, 'route': route}
    return {'status': "Log in", 'route': 'login'}
@view_config(route_name='coxviewer_table', renderer='../templates/coxviewer_table.jinja2')
def coxtable_view(request):
    return {}





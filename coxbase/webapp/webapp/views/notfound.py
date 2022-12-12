from pyramid.view import notfound_view_config
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotAcceptable


@notfound_view_config(renderer="../templates/404.jinja2")
def notfound_view(request):
    request.response.status = 404
    return {}


@view_config(context=HTTPNotAcceptable, renderer="../templates/not_acceptable.jinja2")
def not_acceptable(request):
    return {}

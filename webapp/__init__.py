from pyramid.config import Configurator
from .requests import MyRequest

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings, request_factory=MyRequest) as config:
        config.include('pyramid_chameleon')
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.include('pyramid_mailer')
        config.scan('.views')
        config.scan('.process_request')
        config.add_static_view('deform_static', 'deform:static/')
    return config.make_wsgi_app()

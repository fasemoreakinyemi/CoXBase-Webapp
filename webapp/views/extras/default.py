from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
import colander
from deform import Form
import deform.widget
from sqlalchemy.exc import DBAPIError

from .. import models

class Search_form(colander.MappingSchema):
    sf = colander.SchemaNode(colander.String())
                             #widget=deform.widget.RichTextWidget())

@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):

    try:
        query = request.db1_session.query(models.organism)
        one = query.filter(models.organism.NCBIASSEMBLY ==
                           'GCF_000007765.2').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'Genus': one.GENUS, 'project': 'coxbase_webapp'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


@view_config(route_name='search_page', renderer='../templates/search.jinja2')
def search(request):
    schema = Search_form()
    myform = Form(schema, buttons=('submit',))
    try:
        query = request.db1_session.query(models.organism).all()
       # one = query.filter(models.organism.NCBIASSEMBLY ==
       #                    'GCF_000019885.1').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    if 'submit' in request.params:
            controls = request.POST.items()
            try:
                appstruct = myform.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(form=e.render())
            search_term =  appstruct['sf']
            url = request.route_url('search_results', item=search_term)
            return HTTPFound(url)
    return {'query': query, 'form': myform.render()} #{'ID': one.ID, 'Strain': one.STRAIi}

@view_config(route_name='search_results', renderer='../templates/result.jinja2')
def result(request):
    items = request.matchdict['item']
    try:
        query = request.db1_session.query(models.Features)
        res = query.filter(models.Features.FeatureName.like('%'+items+'%')).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    if not res:
        ur = request.route_url('No_entry', item=items)
        return HTTPFound(ur)
    return {'results': res}

@view_config(route_name='No_entry', renderer='../templates/NoEntry.jinja2')
def missing(request):
    items = request.matchdict['item']
    return {'entry': items}

@view_config(route_name='detailed_view', renderer='../templates/result2.jinja2')
def detailed(request):
    items = request.matchdict['uid']
    try:
        query = request.db1_session.query(models.Features)
        res = query.filter(models.Features.FeatureNum == int(items)).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'results': res}
    


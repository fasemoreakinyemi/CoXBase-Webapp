from pyramid.view import view_config
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from Bio.Blast.Applications import NcbiblastnCommandline
from webapp import models
from webapp import process_request
from webapp import automapper

am = automapper.Automapper("/home/ubuntu/coxbase/coxbase/webapp/development.ini")
base_automap = am.generate_base("db2.")
rp = process_request.RequestProcessor()

# view controller for year plot on dashboard
@view_config(route_name="api_dashboard_year", renderer="json")
def api_dashboard_year(request):
    _column = request.matchdict["ID"]  # _column is country
    isolatesTable = getattr(base_automap, "isolates")
    isolatesRefTable = getattr(base_automap, "isolate_refs2")
    if request.authenticated_userid:
        query = (
            request.db2_session.query(isolatesTable.yearOfIsolation)
            .filter(isolatesTable.country == _column)
            .all()
        )
    else:
        query = (
            request.db2_session.query(isolatesTable.yearOfIsolation)
            .filter(isolatesTable.country == _column)
            .all()
        )
    #  query = request.db2_session.query(model.yearOfIsolation).join(isolatesRef, model.isolateid == isolatesRef.isolate_id).filter(isolatesRef.pmid  == 25037926).filter(
    #           model.country == _column).all()
    result_dict = rp.to_dict(query)
    return result_dict


# view controller for host plot on dashboard
@view_config(route_name="api_dashboard_host", renderer="json")
def api_dashboard_host(request):
    _column = request.matchdict["ID"]  # _column is country
    isolatesTable = getattr(base_automap, "isolates")
    isolatesRefTable = getattr(base_automap, "isolate_refs2")
    if request.authenticated_userid:
        query = (
            request.db2_session.query(isolatesTable.host)
            .filter(isolatesTable.country == _column)
            .all()
        )
    else:
        query = (
            request.db2_session.query(isolatesTable.host)
            .filter(isolatesTable.country == _column).all()
        )
    #      query = request.db2_session.query(model.host).join(isolatesRef, model.isolateid == isolatesRef.isolate_id).filter(isolatesRef.pmid  == 25037926).filter(model.country == _column).all()
    result_dict = rp.to_dict(query)
    return result_dict


# view controller for province plot on dashboard
@view_config(route_name="api_dashboard_province", renderer="json")
def api_dashboard_province(request):
    _column = request.matchdict["ID"]  # _column is country
    isolatesTable = getattr(base_automap, "isolates")
    isolatesRefTable = getattr(base_automap, "isolate_refs2")
    if request.authenticated_userid:
        query = (
            request.db2_session.query(isolatesTable.province)
            .filter(isolatesTable.country == _column)
            .all()
        )
    else:
        query = (
            request.db2_session.query(isolatesTable.province)
            .filter(isolatesTable.country == _column)
            .all()
        )
    #   query = request.db2_session.query(model.province).join(isolatesRef, model.isolateid == isolatesRef.isolate_id).filter(isolatesRef.pmid  == 25037926).filter(model.country == _column).all()
    result_dict = rp.to_dict(query)
    return result_dict


# view controller for genotype plot on dashboard
@view_config(route_name="api_dashboard_genotype", renderer="json")
def api_dashboard_genotype(request):
    _column = request.matchdict["ID"]  # _column is country
    isolatesTable = getattr(base_automap, "isolates")
    isolatesRefTable = getattr(base_automap, "isolate_refs2")
    if request.authenticated_userid:
        query = (
            request.db2_session.query(isolatesTable.mlvaGenotype)
            .filter(isolatesTable.country == _column)
            .all()
        )
    else:
        query = (
            request.db2_session.query(isolatesTable.mlvaGenotype)
            .filter(isolatesTable.country == _column)
            .all()
        )
    #   query = request.db2_session.query(model.mlvaGenotype).join(isolatesRef, model.isolateid == isolatesRef.isolate_id).filter(isolatesRef.pmid  == 25037926).filter(model.country == _column).all()
    result_dict = rp.to_dict(query)
    return result_dict

# plots
@view_config(route_name="api_column", renderer="json")
def api_filter(request):
    RP = process_request.RequestProcessor()
    _column = request.matchdict["column"]
    model = RP.get_model(_column)
    if model:
        try:
            query = request.db2_session.query(model).all()
            result_dict = RP.to_dict(query)
        except DBAPIError:
            return RP.response_error()
        return result_dict
    else:
        return {"NOT": "working"}


@view_config(route_name="api_filter", renderer="json")
def model_filter(request):
    RP = process_request.RequestProcessor()
    _column = request.matchdict["column"]
    model = RP.get_model(_column)
    _filter = request.matchdict["filter"]
    filter_model = RP.get_model_filter(_filter)
    _filter_value = request.matchdict["filter_value"]
    if model:
        try:
            query = (
                request.db2_session.query(model)
                .filter(filter_model == _filter_value)
                .all()
            )
            result_dict = RP.to_dict(query)
        except DBAPIError:
            return RP.response_error()
        return result_dict
    else:
        return {"NOT": "working"}


@view_config(route_name="api_map", renderer="json")
def map_filter(request):
    RP = process_request.RequestProcessor()
    _column = request.matchdict["column"]
    _filter_value = request.matchdict["state"]
    query = request.db2_session.query(models.SampleMetadata)
    model = RP.get_model(_column)
    result = query.filter(model == _filter_value).all()
    return RP._serialize(result)

# eview map for mlva isolates
@view_config(route_name="api_mlva_map", renderer="json")
def get_mlva_coordinates(request):
    geoTable = getattr(base_automap, "isolates_geolocation")
    _column = request.matchdict["ID"]
    query = (
        request.db2_session.query(geoTable)
        .filter(geoTable.mlvaGenotype == _column)
        .all()
    )
    return rp._serialize_coord(query)


# eview map for mst isolates
@view_config(route_name="api_mst_map", renderer="json")
def get_mst_coordinates(request):
    geoTable = getattr(base_automap, "isolates_geolocation")
    _column = request.matchdict["ID"]
    query = (
        request.db2_session.query(geoTable)
        .filter(geoTable.mstGroup == _column)
        .all()
    )
    return rp._serialize_coord(query)

# coxviewer index
@view_config(route_name="api_coxviewer", renderer="json")
def get_geo_details(request):
    isolatesTable = getattr(base_automap, "isolates")
    isolatesRefTable = getattr(base_automap, "isolate_refs2")
    if request.authenticated_userid:
        query = request.db2_session.query(isolatesTable.country).all()
    else:
        query = request.db2_session.query(isolatesTable.country).all()
    #   query = request.db2_session.query(isolates.country).join(isolatesRef, isolates.isolateid == isolatesRef.isolate_id).filter(isolatesRef.pmid  == 25037926).all()

    return rp.to_geoloc_dict(query)

# isolates table per country
@view_config(route_name="api_coxviewer2", renderer="json")
def get_country_details(request):
    country_id = request.matchdict["ID"]
    isolatesTable = getattr(base_automap, "isolates")
    isolatesRefTable = getattr(base_automap, "isolate_refs2")
    # query = request.db2_session.query(isolates).join(isolatesRef, isolates.isolateid == isolatesRef.isolate_id).filter(isolatesRef.pmid  == 25037926).filter(isolates.country == country_id).all()
    query = (
        request.db2_session.query(isolatesTable).filter(isolatesTable.country == country_id).all()
    )
    return rp._serialize_ctr_dts_ls(query)

# blast for new result for new mst
@view_config(route_name="blast_api", renderer="json")
def mst_blast_api(request):
    process_id = request.matchdict["ID"]
    spacer = request.matchdict["spacer"]
    query = "/home/ubuntu/temp/{}/{}.fasta".format(process_id, spacer)
    db = "/home/ubuntu/db/{}.fa".format(spacer)
    cline = NcbiblastnCommandline(
        query=query, db=db, strand="plus", evalue=0.001, out="-", outfmt=0
    )
    return {"result": cline()[0]}

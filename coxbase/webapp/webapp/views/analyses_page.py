#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config


@view_config(route_name="mlvaanalysis", renderer="../templates/mlva_analysis.jinja2")
def mlvaanalysis_view(request):
    return {}


@view_config(route_name="mstanalysis", renderer="../templates/mst_analysis.jinja2")
def mstanalysis_view(request):
    return {}


@view_config(
    route_name="is1111analysis", renderer="../templates/is1111_analysis.jinja2"
)
def is1111analysis_view(request):
    return {}


@view_config(route_name="adaanalysis", renderer="../templates/adaA_analysis.jinja2")
def adaAanalysis_view(request):
    return {}


@view_config(route_name="combined", renderer="../templates/combined_analysis.jinja2")
def combine_view(request):
    return {}

@view_config(route_name="SNPHanalysis", renderer="../templates/hornstra_analysis.jinja2")
def hornstraanalysis_view(request):
    return {}

@view_config(route_name="arg_pred", renderer="../templates/arg_pred_analysis.jinja2")
def arg_pred_analysis_view(request):
    return {}

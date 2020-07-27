#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound, HTTPNotAcceptable


@view_config(route_name="news_api_homepage",
             request_method="GET",
             renderer="../templates/newsAPI.jinja2")
def newsubmission_view(request):
    return {}

@view_config(route_name="news_api",
             renderer="json")
def getnews_view(request):
    from newsapi.newsapi_client import NewsApiClient
    key="fca975d8decb4fca927d66a60c85c4e1"
    newsapi = NewsApiClient(api_key=key)
    searchterm = request.matchdict["search"]
    language = request.matchdict["lang"]
    if language not in ["en", "de"]:
        raise HTTPNotFound()

    headlines = newsapi.get_everything(q=searchterm,
                                          language=language)
    return {"results": headlines}



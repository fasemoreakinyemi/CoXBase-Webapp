#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from .. import models
from pyramid.response import Response

class RequestProcessor():
    __model_dict = {'SampleYear' : models.SampleMetadata.SampleYear,
                    'SampleHost' : models.SampleMetadata.SampleHost,
                    'SampleCountry' : models.SampleMetadata.SampleCountry,
                    'CountryProvince' : models.SampleMetadata.CountryProvince,
                    'SampleSource' : models.SampleMetadata.SampleSource,
                    'PlasmidID' : models.SampleMetadata.PlasmidID,
                    'MSTID' : models.SampleMetadata.MSTID,
                    'MLVAID' : models.SampleMetadata.MLVAID,
                    'TypingID' : models.SampleMetadata.TypingID}

    @classmethod
    def get_model(cls, column_from_path):
        query_model = cls.__model_dict.get(column_from_path, None)
        return query_model
    
    @classmethod
    def get_model_filter(cls, _filter):
        filter_model = cls.__model_dict.get(_filter, None)
        return filter_model

    
    @staticmethod
    def to_dict(args):
        base_count = 1
        _result_dict = {}
        tidy_list = [item for item, in args]
        for items in tidy_list:
            if items:
                if not str(items) in _result_dict:
                    _result_dict[str(items)] = base_count
                else:
                    _result_dict[str(items)] = _result_dict.get(str(items)) + 1
        return _result_dict
    
    @staticmethod
    def _serialize(obj):
        list_container = []
        for items in obj:
            item_dict = {}
            item_dict['name'] = items.SampleStrain
            item_dict['year'] = items.SampleYear
            item_dict['host'] = items.SampleHost
            item_dict['source'] = items.SampleSource
            item_dict['Genotype'] = items.MLVAID
            list_container.append(item_dict)
        return list_container

    
    @staticmethod
    def response_error():
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
        return Response(db_err_msg, content_type='text/plain', status=500)






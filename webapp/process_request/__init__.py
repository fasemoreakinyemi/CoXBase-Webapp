#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from .. import models
from pyramid.response import Response
import pandas as pd
import numpy as np
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base

class RequestProcessor():
    Base = automap_base()
    settings = get_appsettings("/home/ubuntu/coxbase/coxbase/webapp/development.ini", name="main")
    engine = engine_from_config(settings, 'db2.')
    Base.prepare(engine, reflect=True)
    __model_dict = {'SampleYear' : models.SampleMetadata.SampleYear,
                    'SampleHost' : models.SampleMetadata.SampleHost,
                    'SampleCountry' : models.SampleMetadata.SampleCountry,
                    'CountryProvince' : models.SampleMetadata.CountryProvince,
                    'SampleSource' : models.SampleMetadata.SampleSource,
                    'PlasmidID' : models.SampleMetadata.PlasmidID,
                    'MSTID' : models.SampleMetadata.MSTID,
                    'MLVAID' : models.SampleMetadata.MLVAID,
                    'TypingID' : models.SampleMetadata.TypingID}

    __repeat_model_dict_prev = {'ms01' : models.mlvaProfile.ms01,
                           'ms03' : models.mlvaProfile.ms03,
                           'ms20' : models.mlvaProfile.ms20,
                           'ms21' : models.mlvaProfile.ms21,
                           'ms22' : models.mlvaProfile.ms22,
                           'ms23' : models.mlvaProfile.ms23,
                           'ms24' : models.mlvaProfile.ms24,
                           'ms26' : models.mlvaProfile.ms26,
                           'ms27' : models.mlvaProfile.ms27,
                           'ms28' : models.mlvaProfile.ms28,
                           'ms30' : models.mlvaProfile.ms30,
                           'ms31' : models.mlvaProfile.ms31,
                           'ms33' : models.mlvaProfile.ms33,
                           'ms34' : models.mlvaProfile.ms34}

    __repeat_model_dict = {'ms01' : Base.classes.mlva_normalized.ms01,
                           'ms03' : Base.classes.mlva_normalized.ms03,
                           'ms20' : Base.classes.mlva_normalized.ms20,
                           'ms21' : Base.classes.mlva_normalized.ms21,
                           'ms22' : Base.classes.mlva_normalized.ms22,
                           'ms23' : Base.classes.mlva_normalized.ms23,
                           'ms24' : Base.classes.mlva_normalized.ms24,
                           'ms26' : Base.classes.mlva_normalized.ms26,
                           'ms27' : Base.classes.mlva_normalized.ms27,
                           'ms28' : Base.classes.mlva_normalized.ms28,
                           'ms30' : Base.classes.mlva_normalized.ms30,
                           'ms31' : Base.classes.mlva_normalized.ms31,
                           'ms33' : Base.classes.mlva_normalized.ms33,
                           'ms34' : Base.classes.mlva_normalized.ms34}


    @staticmethod
    def check_nonetype_int(item):
        if item == None:
            return None
        else:
            return str(item)
    @staticmethod
    def check_nonetype_str(item):
        if item == None:
            return None
        else:
            return str(float(round(item, 2)))

    @classmethod
    def get_model(cls, column_from_path):
        query_model = cls.__model_dict.get(column_from_path, None)
        return query_model
    
    @classmethod
    def get_model_filter(cls, _filter):
        filter_model = cls.__model_dict.get(_filter, None)
        return filter_model

    @classmethod
    def get_repeat_model(cls, column_from_path):
        query_model = cls.__repeat_model_dict.get(column_from_path, None)
        return query_model
    
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
    def to_geoloc_dict(args):
        file_path = '/home/ubuntu/countries.csv'
        geofile = pd.read_csv(file_path, sep=",")
        base_count = 1
        _result_dict = {}
        tidy_list = [item for item, in args]
        for items in tidy_list:
            if items:
                if not str(items) in _result_dict:
                    _result_dict[str(items)] = base_count
                else:
                    _result_dict[str(items)] = _result_dict.get(str(items)) + 1
        list_container = []
        for keys in _result_dict:
            item_dict = {}
            query = geofile.loc[geofile['country'] == keys] #geofile.query("country=='{}'".format(keys))
            item_dict['ID'] = keys
            item_dict['count'] = str(_result_dict.get(keys, None))
            item_dict['name'] = str("".join(list(query['name'].values)))
            item_dict['lat'] = "".join(map(str, query['latitude'].values))
            item_dict['long'] = "".join(map(str, query['longitude'].values))
            if item_dict['name'] == "":
                continue
            else:
                list_container.append(item_dict)
        return list_container
    # json for front end table
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
    # mlva result to json serializer
    @classmethod
    def _serialize_mlva(cls, obj):
        list_container = []
        for items in obj:
            item_dict = {}
            item_dict['Genotype'] = items.ngt
            item_dict['ms01'] = cls.check_nonetype_int(items.ms01)
            item_dict['ms03'] = cls.check_nonetype_int(items.ms03)
            item_dict['ms20'] = cls.check_nonetype_str(items.ms20)
            item_dict['ms21'] = cls.check_nonetype_int(items.ms21)
            item_dict['ms22'] = cls.check_nonetype_int(items.ms22)
            item_dict['ms23'] = cls.check_nonetype_int(items.ms23)
            item_dict['ms24'] = cls.check_nonetype_int(items.ms24)
            item_dict['ms26'] = cls.check_nonetype_int(items.ms26)
            item_dict['ms27'] = cls.check_nonetype_int(items.ms27)
            item_dict['ms28'] = cls.check_nonetype_int(items.ms28)
            item_dict['ms30'] = cls.check_nonetype_str(items.ms30)
            item_dict['ms31'] = cls.check_nonetype_int(items.ms31)
            item_dict['ms33'] = cls.check_nonetype_int(items.ms33)
            item_dict['ms34'] = cls.check_nonetype_int(items.ms34)
            list_container.append(item_dict)
        return list_container
    # mst results to json serializer
    @staticmethod
    def _serialize_mst(obj):
        list_container = []
        for items in obj:
            item_dict = {}
            item_dict['MST ID'] = int(items.groupid)
            item_dict['cox2'] = int(items.COX2)
            item_dict['cox5'] = int(items.COX5)
            item_dict['cox18'] = int(items.COX18)
            item_dict['cox20'] = int(items.COX20)
            item_dict['cox22'] = int(items.COX22)
            item_dict['cox37'] = int(items.COX37)
            item_dict['cox51'] = int(items.COX51)
            item_dict['cox56'] = int(items.COX56)
            item_dict['cox57'] = int(items.COX57)
            item_dict['cox61'] = int(items.COX61)
            list_container.append(item_dict)
        return list_container
    # geographical details for map
    @staticmethod
    def _serialize_coord(obj):
        list_container = []
        for items in obj:
            item_dict = {}
            item_dict['ID'] = items.ID
            item_dict['name'] = items.name
            item_dict['lat'] = str(items.latitude)
            item_dict['long'] = str(items.longitude)
            list_container.append(item_dict)
        return list_container
   
   # country list for coxviewer
    @staticmethod
    def _serialize_ctr_dts(obj):
        list_container = []
        for items in obj:
            item_dict = {}
            item_dict['name'] = items.name
            item_dict['doi'] = str(items.yearOfIsolation)
            item_dict['host'] = items.host
            item_dict['source'] = items.tissue
            item_dict['location'] = items.geographicOrigin
            item_dict['province'] = items.province
            item_dict['plasmid'] = items.plasmidType
            item_dict['adagene'] = items.adaGene
            item_dict['mlva'] = items.mlvaGenotype
            item_dict['mst'] = items.mstGroup
            item_dict['isgroup'] = items.isGroup
            list_container.append(item_dict)
        return list_container
   
   # country list for coxviewer list method
    @staticmethod
    def _serialize_ctr_dts_ls(obj):
        list_container = []
        for items in obj:
            item_list = []
            item_list.append(items.name)
            item_list.append(str(items.yearOfIsolation))
            item_list.append(items.host)
            item_list.append(items.tissue)
            item_list.append(items.geographicOrigin)
            item_list.append(items.province)
            item_list.append(items.plasmidType)
            item_list.append(items.adaGene)
            item_list.append(items.mlvaGenotype)
            item_list.append(items.mstGroup)
            item_list.append(items.isGroup)
            list_container.append(item_list)
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






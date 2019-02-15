#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import YEAR

Base = declarative_base()

class SampleMetadata(Base):
    __tablename__ = "SampleMetadata"
    ID = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    Strain = Column(String(30))
    SampleName = Column(String(30))
    SampleYear = Column(YEAR(4))
    SampleHost = Column(String(30))
    SampleSource = Column(String(50))
    SampleCountry = Column(String(30))
    CountryProvince = Column(String(50))
    Latitude = Column(DECIMAL(10,8))
    Longtitude = Column(DECIMAL(11,8))
    Publication = Column(String(200))
    PubmedID = Column(Integer())
    TypingID = Column(Integer, ForeignKey("TypingMetaData.ID"), nullable=False)
    MLVAID = Column(Integer, ForeignKey("MLVAProfile.ID"), nullable=False)


class TypingMetaData(Base):
    __tablename__ = "TypingMetadata"
    ID = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    PanelType = Column(String(30), nullable=False)
    PlasmidType = Column(String(15))
    MSTType = Column(String(30))
    ClusterType = Column(String(5))
    Genotype = Column(String(10))

class MLVAProfile(Base):
    __tablename__ = "MLVAProfile"
    ID = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    MS01 = Column(Integer())
    MS03 = Column(Integer())
    MS20 = Column(Integer())
    MS21 = Column(Integer())
    MS22 = Column(Integer())
    MS23 = Column(Integer())
    MS24 = Column(Integer())
    MS26 = Column(Integer())
    MS27 = Column(Integer())
    MS28 = Column(Integer())
    MS30 = Column(Integer())
    MS31 = Column(Integer())
    MS33 = Column(Integer())
    MS34 = Column(Integer())

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/cox')
Base.metadata.create_all(engine)


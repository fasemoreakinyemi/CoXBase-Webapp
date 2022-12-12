#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import YEAR

Base = declarative_base()


class plasmid(Base):
    __tablename__ = "Plasmid"
    ID = Column(Integer, nullable=False, primary_key=True)
    PlasmidType = Column(String(15))

class mst(Base):
    __tablename__ = "MST"
    ID = Column(Integer, nullable=False, primary_key=True)
    MSTType = Column(String(30))


class TypingMeta(Base):
    __tablename__ = "TypingMetadata"
    ID = Column(Integer, nullable=False, primary_key=True)
    ClusterType = Column(String(5))
    Genotype = Column(String(10))

class SampleMetadata(Base):
    __tablename__ = "SampleMetadata"
    ID = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    SampleStrain = Column(String(50))
    SampleYear = Column(YEAR(4))
    SampleHost = Column(String(30))
    SampleSource = Column(String(100))
    SampleCountry = Column(String(30))
    CountryProvince = Column(String(100))
    Latitude = Column(DECIMAL(10,8))
    Longitude = Column(DECIMAL(11,8))
    PubmedID = Column(Integer())
    PlasmidID = Column(Integer, ForeignKey("Plasmid.ID"), nullable=False)
    MSTID = Column(Integer, ForeignKey("MST.ID"), nullable=False)
    TypingID = Column(Integer, ForeignKey("TypingMetadata.ID"), nullable=False)
    MLVAID = Column(Integer, ForeignKey("MLVAProfile.ID"), nullable=False)

class mlvaProfile(Base):
    __tablename__ = "MLVAProfile"
    ID = Column(Integer, nullable=False, primary_key=True)
    PanelType = Column(String(30), nullable=False)
    ms01 = Column(Float(10,2))
    ms03 = Column(Float(10,2))
    ms20 = Column(Float(10,2))
    ms21 = Column(Float(10,2))
    ms22 = Column(Float(10,2))
    ms23 = Column(Float(10,2))
    ms24 = Column(Float(10,2))
    ms26 = Column(Float(10,2))
    ms27 = Column(Float(10,2))
    ms28 = Column(Float(10,2))
    ms30 = Column(Float(10,2))
    ms31 = Column(Float(10,2))
    ms33 = Column(Float(10,2))
    ms34 = Column(Float(10,2))

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/MLVA')
Base.metadata.create_all(engine)


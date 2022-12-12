#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class organism(Base):
    __tablename__ = "Organisms"
    ID = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    GENUS = Column(String(30), nullable=False)
    SPECIES = Column(String(30), nullable=False)
    CHROMOSOME = Column(String(30))
    PUBMEDNUM = Column(String(50))
    NCBIASSEMBLY = Column(String(50))
    STRAIN = Column(String(300))

class Features(Base):
    __tablename__ = "FeatureAttributes"
    FeatureNum = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    FeatureChromosome = Column(String(30), nullable=False)
    FeatureID = Column(String(15), nullable=False)
    FeatureName = Column(String(30))
    FeatureType = Column(String(30))
    FeatureStart = Column(Integer())
    FeatureEnd = Column(Integer())
    FeatureStrand = Column(String(3))
    Parent = Column(String(15))
    ParentID = Column(String(15))
    LocusTag = Column(String(20))
    DbxrefDatabase = Column(String(30))
    DbxrefIdentifier = Column(String(40))
    ProteinID = Column(String(40))
    ProteinProduct = Column(String(500))
    OrganismID = Column(Integer, ForeignKey("Organisms.ID"), nullable=False)

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/cox')
Base.metadata.create_all(engine)


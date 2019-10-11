#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Float, VARBINARY, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import YEAR

Base = declarative_base()



class SubmissionTable(Base):
    __tablename__ = "SubmissionTable"
    ID = Column(String(36), nullable=False, primary_key=True)
    SubmissionDate = Column(DateTime(timezone=True), server_default=func.now())
    User = Column(String(100), nullable=True)
    AnalysisType = Column(String(25), nullable=True)
    IPaddress= Column(String(16), nullable=True)

class isolateSubmission(Base):
    __tablename__ = "isolateSubmission"
    ID = Column(String(36), nullable=False, primary_key=True)
    submissionType = Column(String(10), nullable=False)
    SubmissionDate = Column(DateTime(timezone=True), server_default=func.now())
    isolateName = Column(String(100), nullable=True)
    isolateSource = Column(String(100), nullable=True)
    isolateHost = Column(String(100), nullable=True)
    placeOfIsolation = Column(String(100), nullable=True)
    yearOfIsolation = Column(YEAR(4))
    country = Column(String(100), nullable=True)
    latitude = Column(DECIMAL(10,8))
    longitude = Column(DECIMAL(11,8))
    pubmedID = Column(String(50), nullable=True)
    genomeAccession = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True)
    submitterName = Column(String(255), nullable=True)


class mlvaSubmission(Base):
    __tablename__ = "mlvaSubmission"
    ID = Column(String(36), nullable=False, primary_key=True)
    ms01 = Column(Float(10,2), nullable=True)
    ms03 = Column(Float(10,2), nullable=True)
    ms20 = Column(Float(10,2), nullable=True)
    ms21 = Column(Float(10,2), nullable=True)
    ms22 = Column(Float(10,2), nullable=True)
    ms23 = Column(Float(10,2), nullable=True)
    ms24 = Column(Float(10,2), nullable=True)
    ms26 = Column(Float(10,2), nullable=True)
    ms27 = Column(Float(10,2), nullable=True)
    ms28 = Column(Float(10,2), nullable=True)
    ms30 = Column(Float(10,2), nullable=True)
    ms31 = Column(Float(10,2), nullable=True)
    ms33 = Column(Float(10,2), nullable=True)
    ms34 = Column(Float(10,2), nullable=True)
    isolateID = Column(String(36), ForeignKey("isolateSubmission.ID"), nullable=False)


class mstSubmission(Base):
    __tablename__ = "mstSubmission"
    ID = Column(String(36), nullable=False, primary_key=True)
    cox18 = Column(Integer(), nullable=True)
    cox2 = Column(Integer(), nullable=True)
    cox20 = Column(Integer(), nullable=True)
    cox22 = Column(Integer(), nullable=True)
    cox37 = Column(Integer(), nullable=True)
    cox5 = Column(Integer(), nullable=True)
    cox51 = Column(Integer(), nullable=True)
    cox56 = Column(Integer(), nullable=True)
    cox57 = Column(Integer(), nullable=True)
    cox61 = Column(Integer(), nullable=True)
    isolateID = Column(String(36), ForeignKey("isolateSubmission.ID"), nullable=False)


engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/MLVA')
Base.metadata.create_all(engine)


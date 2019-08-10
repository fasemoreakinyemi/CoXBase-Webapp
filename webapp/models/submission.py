#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Float, VARBINARY, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func

Base = declarative_base()



class SubmissionTable(Base):
    __tablename__ = "SubmissionTable"
    ID = Column(String(36), nullable=False, primary_key=True)
    SubmissionDate = Column(DateTime(timezone=True), server_default=func.now())
    User = Column(String(100), nullable=True)
    AnalysisType = Column(String(25), nullable=True)
    IPaddress= Column(String(16), nullable=True)

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/MLVA')
Base.metadata.create_all(engine)


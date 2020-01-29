#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import TINYINT

Base = declarative_base()

class adaAProfile(Base):
    __tablename__ = "adaAProfile"
    ID = Column(String(36), nullable=False, primary_key=True)
    adaAStatus = Column(TINYINT(1))
    genotype = Column(String(30))
    plasmidType = Column(String(20))

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/MLVA')
Base.metadata.create_all(engine)


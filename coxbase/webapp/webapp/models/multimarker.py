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

class multimarker(Base):
    __tablename__ = "multimarker_profile"
    ID = Column(Integer, nullable=False, primary_key=True)
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
    ms01 = Column(Integer(), nullable=True)
    ms03 = Column(Integer(), nullable=True)
    ms20 = Column(Integer(), nullable=True)
    ms21 = Column(Integer(), nullable=True)
    ms22 = Column(Integer(), nullable=True)
    ms23 = Column(Integer(), nullable=True)
    ms24 = Column(Integer(), nullable=True)
    ms26 = Column(Integer(), nullable=True)
    ms27 = Column(Integer(), nullable=True)
    ms28 = Column(Integer(), nullable=True)
    ms30 = Column(Integer(), nullable=True)
    ms31 = Column(Integer(), nullable=True)
    ms33 = Column(Integer(), nullable=True)
    ms34 = Column(Integer(), nullable=True)

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/MLVA')
Base.metadata.create_all(engine)


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
class mstSpacerResult(Base):
    __tablename__ = "mstSpacerResultTable"
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

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/MLVA')
Base.metadata.create_all(engine)


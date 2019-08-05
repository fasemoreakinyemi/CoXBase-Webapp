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



class ProductLength(Base):
    __tablename__ = "ProductLengthISPCR"
    ID = Column(String(36), nullable=False, primary_key=True)
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

class FlankLength(Base):
    __tablename__ = "FlankLengthISPCR"
    ID = Column(String(36), ForeignKey("ProductLengthISPCR.ID"), nullable=False, primary_key=True)
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

class RepeatSize(Base):
    __tablename__ = "RepeatSizeISPCR"
    ID = Column(String(36), ForeignKey("ProductLengthISPCR.ID"), nullable=False, primary_key=True)
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

class RepeatNumber(Base):
    __tablename__ = "RepeatNumberISPCR"
    ID = Column(String(36), ForeignKey("ProductLengthISPCR.ID"), nullable=False, primary_key=True)
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


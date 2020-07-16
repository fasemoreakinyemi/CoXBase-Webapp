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

class snpHornstra(Base):
    __tablename__ = "snpHornstra"
    ID = Column(String(36), nullable=False, primary_key=True)
    Cox5bp81 = Column(String(1))
    Cox22bp91 = Column(String(1))
    Cox18bp376 = Column(String(1))
    Cox51bp356 = Column(String(1))
    Cox18bp34 = Column(String(1))
    Cox5bp109 = Column(String(1))
    Cox22bp118 = Column(String(1))
    Cox51bp492 = Column(String(1))
    Cox57bp327 = Column(String(1))
    Cox56bp10 = Column(String(1))
    Cox51bp67 = Column(String(1))
    Cox20bp155 = Column(String(1))

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/MLVA')
Base.metadata.create_all(engine)


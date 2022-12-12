#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, Float, VARBINARY, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import YEAR

Base = declarative_base()



class accessTable(Base):
    __tablename__ = "accessTable"
    ID = Column(String(36), nullable=False, primary_key=True)
    accessDate = Column(DateTime(timezone=True), server_default=func.now())
    view_name = Column(String(200), nullable=True)
    user_ip= Column(String(16), nullable=True)

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/MLVA')
Base.metadata.create_all(engine)


#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import YEAR

Base = declarative_base()



class UserTable(Base):
    __tablename__ = "UserTable"
    ID = Column(String(36), nullable=False, primary_key=True)
    email = Column(String(255), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(60), nullable=False)
    group = Column(String(100), nullable=True)

engine = create_engine('mysql+pymysql://burnetii:crazyburnetii@localhost/MLVA')
Base.metadata.create_all(engine)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Table, Column, MetaData

import pymysql
from sqlalchemy.sql.sqltypes import Integer, String

# import MySQLdb


#create db connection
engine = create_engine("mysql+pymysql://dwzq:dwzq1234@127.0.0.1:3306/quant_db", max_overflow=5)

#get metadata
metadata = MetaData()

#define table
user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(20)))

#create table if it doesn't exist
metadata.create_all(engine)


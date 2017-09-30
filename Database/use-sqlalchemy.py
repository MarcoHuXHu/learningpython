#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SQLAlchemy是一种常用的ORM框架，基本用法如下

from sqlalchemy import Column, String, Integer, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 自定义对象，与数据库中的table对应:
class Food(Base):
    # 对应table的名字:
    __tablename__ = 'food'
    # schema of table:
    food_id = Column(Integer, primary_key=True)
    name = Column(String(45))
    unit = Column(Integer)
    unit_name = Column(String(40))
    # energy = Column(Float)
    carbohydrate = Column(Float)
    protein = Column(Float)
    fat = Column(Float)

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:password@localhost:3306/food_nutrition')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()

food = session.query(Food).filter(Food.food_id==1).one()
print(food.name) # Whey

session.close()
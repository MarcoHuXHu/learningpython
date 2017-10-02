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
# 在connect string后面+'?charset=utf8'可以使得中文正常使用
engine = create_engine('mysql+pymysql://root:password@localhost:3306/food_nutrition?charset=utf8')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()

# 更新数据
food = session.query(Food).filter(Food.name=='蛋白').one()
food.unit = 100
food.unit_name = 'g'
food.carbohydrate = 3.1
food.protein = 11.6
food.fat = 0.1

session.commit()

session.close()


# 一对多和多对一

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
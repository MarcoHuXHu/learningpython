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

def example1():
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

    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    passwd = Column(String(50))
    image = Column(String(500))
    name = Column(String(50))
    # 一对多:
    blogs = relationship('Blog')

class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    summary = Column(String(200))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(50), ForeignKey('user.id'))
    user = relationship('User')


def example2():
    # 初始化数据库连接:
    # 在connect string后面+'?charset=utf8'可以使得中文正常使用
    engine = create_engine('mysql+pymysql://root:password@localhost:3306/awesome?charset=utf8')

    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    session = DBSession()
    # 新建数据
    # u1 = User(name='Ann', email='ann@example.com', passwd='1234567890', image='about:blank')
    # u2 = User(name='Ben', email='ben@example.com', passwd='1234567890', image='about:blank')
    # u3 = User(name='Cat', email='cat@example.com', passwd='1234567890', image='about:blank')
    # session.add(u1)
    # session.add(u2)
    # session.add(u3)
    # # 更新数据
    # b1 = Blog(name='Blog1', user_id=1, summary='Hello Ann')
    # b2 = Blog(name='Blog2', user_id=2, summary='Hello Ben')
    # b3 = Blog(name='Blog3', user_id=3, summary='Hello Cat')
    # b4 = Blog(name='Blog4', user_id=1, summary='Hello World')
    # b5 = Blog(name='Blog5', user_id=1, summary='Hello World Again')
    # for b in [b1,b2,b3,b4,b5]:
    #     session.add(b)

    # 1 to n mapping查找
    user = session.query(User).filter(User.name == 'Ann').one()
    for blog in user.blogs:
        print('User: %s ; Blog: %s ; Summary: %s' % (user.name, blog.name, blog.summary))
    # User: Ann ; Blog: Blog1 ; Summary: Hello Ann
    # User: Ann ; Blog: Blog4 ; Summary: Hello World
    # User: Ann ; Blog: Blog5 ; Summary: Hello World Again

    # n to 1 mapping查找
    blog = session.query(Blog).filter(Blog.summary == 'Hello Cat').one()
    blog_user = blog.user
    print('%s, %s' % (blog_user.name, blog_user.email)) # Cat, cat@example.com

    session.close()


example2()
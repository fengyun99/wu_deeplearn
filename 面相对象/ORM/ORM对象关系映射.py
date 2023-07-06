#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/6 11:14
# @Author   : FengYun
# @File     : ORM对象关系映射.py
# @Software : PyCharm
# 使用SQLAlchemy将对象自动映射到数据库中
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql

engine = create_engine("mysql+pymysql://username:password@ipaddress:3306/dbtest?charset=utf8", max_overflow=5)

# 定义缓存对象
Session = sessionmaker(bind=engine)
session = Session()
# 声明基类，包含ORM映射中相关的类和表的信息
Base = declarative_base()


# 基于基类创建自定义类，类就是表
class Person(Base):
    __tablename__ = 'mydata'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    email = Column(String(32), unique=True)

    def __repr__(self):
        return "<Person(name='%s')>" % self.name


if __name__ == '__main__':
    # 检查数据库是否存在不存在创建
    Base.metadata.create_all(engine)
    # 添加单条数据
    person = Person(name="王小明")
    person.email = "wangxiaoming@mi.com"
    # 添加person对象，但是还没提交到数据库
    session.add(person)
    # 提交
    session.commit()


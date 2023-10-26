#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/24 16:49
# @Author   : FengYun
# @File     : 类方法.py
# @Software : PyCharm
# 静态方法也叫类方法
# 静态方法类似于一个公共的共享资源，他不会被自动销毁，会一直在内存中。实例类则会自动销毁。
# 静态方法存储于静态存储区，他使用static关键字来修饰的方法即为静态方法，静态方法可被继承，但不可被重写而是隐藏，静态类中的所有成员也必须是静态。 非静态类中的成员可以是静态也可以是非静态。

class People(object):
    country = 'china'

    # 类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

    # 通过类方法更改类属性
    @classmethod
    def setCountry(cls, country):
        cls.country = country


p = People()
print(p.getCountry())  # 可以用过实例对象引用
print(People.getCountry())  # 可以通过类对象引用
# 通过类方法更改类属性
p.setCountry('japan')
print(p.getCountry())
print(People.getCountry())

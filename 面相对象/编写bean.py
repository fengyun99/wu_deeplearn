#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/5 11:26
# @Author   : FengYun
# @File     : 编写bean.py
# @Software : PyCharm

class MyData:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def get_name(self):
        return self._name

    @property
    def get_age(self):
        return self._age

    @get_name.setter
    def get_name(self, name):
        self._name = name

    @get_age.setter
    def get_age(self, age):
        self._age = age

    def __str__(self):
        return f"名字是:{self._name}\n年龄是:{self._age}"

    # 编写后两个对象内容相同，则为True
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


if __name__ == '__main__':
    mydata = MyData("Alex", 17)
    print(mydata)
    # get
    print(mydata.get_name)
    # set
    mydata.get_name = "Bob"
    print(mydata)
    bbb = MyData("Bob", 17)
    print(bbb)
    print(mydata == bbb)

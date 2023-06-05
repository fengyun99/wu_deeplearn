#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/5 11:45
# @Author   : FengYun
# @File     : 通过json判断对象是否一致.py
# @Software : PyCharm
import json


class MyData:
    class Address:
        def __init__(self, area, city, parent: dict):
            self._area = area
            self._city = city
            self._parent = parent

    # set不存在__dict__需要转为其他类型
    # 元组，列表需要排序再判断
    # 字典可以直接判断
    def __init__(self, name, age, area, city, parent: dict, game: list, test: dict, setbox: set[int]):
        self._address = self.Address(area, city, parent)
        self._name = name
        self._age = age
        self._game = sorted(game)
        self._test = test
        self._setbox = sorted(setbox)

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

    @property
    def get_address(self):
        return self._address

    @get_address.setter
    def get_address(self, value):
        # 解包两个值
        area, city = value
        self._address = self.Address(area, city)

    def __str__(self):
        return f"名字是:{self._name}\n年龄是:{self._age}\n地址是:{self._address}"

    # # 之前的方案测试
    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__


# 不重写equals，就会无法判断，不json化就没法判断内部类
if __name__ == '__main__':
    mydata1 = MyData("Li", 15, "cn", "sh", {"m":"w", "b": "z"}, ["a", "b", "c", "1"], {"a": 1, "b": 2}, {1, 2, 3, 3})
    mydata2 = MyData("Li", 15, "cn", "sh", {"m":"w", "b": "z"}, ["c", "a", "b", "1"], {"b": 2, "a": 1}, {3, 2, 1})
    a = json.dumps(mydata1, default=lambda obj: obj.__dict__, sort_keys=True)
    print(a)
    b = json.dumps(mydata2, default=lambda obj: obj.__dict__, sort_keys=True)
    print(b)
    # 判断值是否相等
    print(a == b)
    # 判断引用的对象是否是同一对象，比较的是地址
    print(a is b)
    print(mydata1 == mydata2)
    print(mydata1 is mydata2)

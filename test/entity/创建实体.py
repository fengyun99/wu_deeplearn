#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 15:34
# @Author   : FengYun
# @File     : 创建实体.py
# @Software : PyCharm
from StudentBuilder import StudentBuilder


class student_info:
    def __init__(self):
        self.builder = None

    def conf_student(self):
        self.builder = StudentBuilder(("银杏", "一栋", 266,),(10, 25, 25, 0, 100, {"辣条": 2, "可乐": 2},))
        self.builder.conf_student("陈家威", 18, "大一", 2000, ["程序", "科学"], ["球队"])

    @property
    def student(self):
        return self.builder.student

if __name__ == '__main__':
    a = student_info()
    print(a.student)
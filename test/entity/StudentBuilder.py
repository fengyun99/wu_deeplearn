#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/11 15:12
# @Author   : FengYun
# @File     : StudentBuilder.py
# @Software : PyCharm
from test.entity.Student import Student


class StudentBuilder:
    def __init__(self, address, biil):
        self.student = Student(address, biil)

    def conf_student(self, name: str, age: int, grade: str, month_pocket_money: int, lesson: list, organize: list):
        self.student.name = name
        self.student.age = age
        self.student.grade = grade
        self.student.month_pocket_money = month_pocket_money
        self.student.lesson = lesson
        self.student.organize = organize

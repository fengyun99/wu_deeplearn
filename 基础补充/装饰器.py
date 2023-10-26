#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 22:54
# @Author   : FengYun
# @File     : 装饰器.py
# @Software : PyCharm
class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter # 不写内容则为只读属性
    def score(self, value):
        if not isinstance(value, int):
            print('成绩必须是整数')
        else:
            if value < 0 or value > 100:
                print('成绩必须在 0-100 之间')
            else:
                self.__score = value


s = Student()
s.score = 60  # 实际转化为 s.set_score(60)
print('获取的成绩是:', s.score)  # 实际转化为 s.get_score()
s.score = 1000
s.score = 'abc'

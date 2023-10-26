#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/20 15:25
# @Author   : FengYun
# @File     : 01.py
# @Software : PyCharm
import operator


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'name:' + self.name


s1 = Student('tony')
print(s1)
print(type(repr('123abc')))
print(type(repr(s1)))  # 对象转换为表达式字符串
str1 = "{'a':1}"
print(type(eval(str1)))

a = '100'  # 此时a的类型是一个字符串，里面存放了100这3个字符
b = int(a)  # 此时b的类型是整型，里面存放的是数字100
print("a=%d" % b)

userName = 'ring'
import keyword

# 关键字有哪些
print(keyword.kwlist)

print(1 and 0)
print(1 or 0)
print(not 1)

print(1 & 0)
print(1 | 0)

# 左对齐
a = '11'
print(a.ljust(5, '0'))

a = 'hello tom you are fine'
print(a.partition('tom'))

aStr = 'a b \ttmmy\naa\nnn\ttyi io \t o \n\n www'
# 存在\n\t空格字符串取倒数第二个字符
print([d for d in aStr.replace('\n', ' ').replace('\t', ' ').split(' ') if d != ''][-2])

a = 'abcd'
print(a[::-1])
# append整体,extend是单个添加
a = [1, 2]
b = [3, 4]
a.append(b)
print(a)
a.extend(b)
print(a)

movieName = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
print('------删除之前------')
for tempName in movieName:
    print(tempName)
del movieName[2]
print('------删除之后------')
for tempName in movieName:
    print(tempName)

# cmp变operator
print(operator.lt('a', 'b'))  # 小于

a = 1
print(a)
del a

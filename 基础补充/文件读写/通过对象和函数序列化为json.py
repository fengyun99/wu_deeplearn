#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 21:37
# @Author   : FengYun
# @File     : 通过对象和函数序列化为json.py
# @Software : PyCharm
# import json
#
#
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#
# # 定义类实例转换为字典的方法
# def student_dict(stu):
#     return {"name": stu.name, "age": stu.age, "score": stu.score}
#
#
# # 创建实例对象
# stu = Student('张三', 23, 98)
# # 将 Student 类的实例转换为 JSON 字符串，ensure_ascii 关键字参数的值设置为 False，
# # 可以让返回的 JSON 字符串正常显示中文
# jsonStr = json.dumps(stu, default=student_dict, ensure_ascii=False)
# print(jsonStr)
import json


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return '姓名是：{0},年龄是：{1},成绩是:{2}'.format(self.name, self.age, self.score)


# 定义类实例转换为字典的方法
def student_dict(stu):
    return {"name": stu.name, "age": stu.age, "score": stu.score}


# 定义将字典转换为实例对象的函数
def jsonToStudent(dic):
    return Student(dic['name'], dic['age'], dic['score'])


# 创建实例类列表
stu1 = Student("张三", 23, 98)
stu2 = Student("李四", 20, 99)
stu3 = Student("王五", 22, 88)
stuList = [stu1, stu2, stu3]
# 将 Student 对象列表转换为 JSON 字符串
stuString = json.dumps(stuList, default=student_dict, ensure_ascii=False)
# 将 JSON 字符串转换为 Student 对象列表
stuList = json.loads(stuString, object_hook=jsonToStudent)
for stu in stuList:
    print(stu)  # 对象

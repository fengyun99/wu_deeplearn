#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/22 17:03
# @Author   : FengYun
# @File     : 学生管理.py
# @Software : PyCharm
student_dict = {}
student_dict_list = []


def add_info(name, age, ids):
    student_dict['name'] = name
    student_dict['age'] = age
    student_dict['ids'] = ids
    student_dict_list.append(student_dict)


def search_info(ids):
    for student_info in student_dict_list:
        if student_info['ids'] == ids:
            return student_info


def delete_info(ids):
    for student_info in student_dict_list:
        if student_info['ids'] == ids:
            del student_info


def change_info(ids):
    for student_info in student_dict_list:
        if student_info['ids'] == ids:
            name = input('name:')
            age = input('age:')
            student_info['name'] = name
            student_info['age'] = age


def main():
    while True:
        q = input('choice:')
        if q == 'q':
            break
        elif q == '1':
            name = input('add name:')
            age = input('add age:')
            ids = input('add ids:')
            add_info(name, age, ids)
        elif q == '2':
            ids = input('delete ids:')
            delete_info(ids)
        elif q == '3':
            ids = input('search ids:')
            print(search_info(ids))
        elif q == '4':
            ids = input('change ids:')
            change_info(ids)


if __name__ == '__main__':
    main()

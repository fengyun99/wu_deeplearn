#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/9/10 10:30
# @Author   : FengYun
# @File     : One-Hot.py
# @Software : PyCharm
import nltk

# 独热编码
str1 = 'Time flies like an arrow.Fruit flies like a banana.'
string_list = [s.lower() for s in str1.replace('.', ' ').split(' ') if s != '']
string_set = []
for s in string_list:
    if s not in string_set:
        string_set.append(s)
print(string_set)
str02 = 'like a banana'
s2_list = str02.split(' ')
one_hot = [0] * len(string_set)
for i in range(len(string_set)):
    for j in s2_list:
        if string_set[i] == j:
            one_hot[i] = 1
print(one_hot)

# tf 词表出现了几次，onehot重合解释
str3 = 'Fruit flies like time flies a fruit'
s3_list = str3.lower().split(' ')

# IDF

# TF-IDF(TF*IDF)



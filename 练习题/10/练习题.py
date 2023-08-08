#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/31 17:07
# @Author   : FengYun
# @File     : 练习题.py
# @Software : PyCharm

# 判断敏感词
def word_test(input):
    with open('filter_word.txt', 'r', encoding='utf-8') as f:
        filter_word_list = [word.replace('\n', '') for word in f.readlines()]
    print(filter_word_list)
    for filter_word in filter_word_list:
        if filter_word in input:
            return 'Freedom'
    return 'Human Rights'


# 敏感词替换为*
def word_replacement(input):
    with open('filter_word.txt', 'r', encoding='utf-8') as f:
        filter_word_list = [word.replace('\n', '') for word in f.readlines()]
    print(filter_word_list)
    for filter_word in filter_word_list:
        if filter_word in input:
            return input.replace(filter_word, '*' * len(filter_word))
    return input


if __name__ == '__main__':
    print(word_replacement('你の妈的'))

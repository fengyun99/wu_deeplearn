#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/23 16:44
# @Author   : FengYun
# @File     : 拆分长字符串.py
# @Software : PyCharm
import re


def main():
    poem = '你好，请问你的名字是叫小明还是小王。我这边需要登记下你的名字。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']


if __name__ == '__main__':
    main()

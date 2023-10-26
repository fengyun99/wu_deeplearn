#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/23 14:43
# @Author   : FengYun
# @File     : read_docx.py
# @Software : PyCharm
from langchain.document_loaders import UnstructuredFileLoader


def remove_attachments(strings_list):
    keywords = ["附件", "附表", "附录"]
    index = 0

    for string in strings_list:
        # 判断字符串是否以关键词开头
        index += 1
        if any(string.startswith(keyword) for keyword in keywords):
            return index
    return len(strings_list)


def find_chinese_mulu(strings_list):
    keywords = ["目录"]
    index = 0

    for string in strings_list:
        # 判断字符串是否以关键词开头
        index += 1
        if any(string.startswith(keyword) for keyword in keywords):
            return index


loader = UnstructuredFileLoader(r'G:\test\住房公积金管理条例.docx')
doc = loader.load()
print(doc[0])
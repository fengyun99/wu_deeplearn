#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/11 13:56
# @Author   : FengYun
# @File     : data_clean.py
# @Software : PyCharm
import re


# 取出html的标签
def remove_html_label(content):
    pattern = re.compile(r'<[^>]+>')
    result = pattern.sub('', content)
    return result

def remove_useless_information(content):
    pattern = re.compile(r'^备用.+')
    result = pattern.sub('',content)
    return result

def stitching_text_with_limit_length(text_list: list):
    list1 = []
    all_text = ''.join(text_list)
    length = len(all_text)
    for i in range(0,length+512,512):
        list1.append(all_text[i:i+512])
    return list1


if __name__ == '__main__':
    with open("data/out.txt", "r", encoding="gbk") as f:
        content = f.read()
    text = remove_html_label(content)
    text_list = text.split("\n")
    out_list = []
    for i in text_list:
        i = remove_useless_information(i.strip())
        if i != '' and not i.isalnum():
            out_list.append(i.strip())
    out = stitching_text_with_limit_length(out_list)
    with open("split_data.txt","a",encoding="gbk") as f:
        for i in out:
            f.writelines(i)
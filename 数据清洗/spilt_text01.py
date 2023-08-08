#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/8 15:40
# @Author   : FengYun
# @File     : spilt_text01.py
# @Software : PyCharm
import re
from typing import List
import PyPDF2


def split_text(pdf_content) -> List[str]:
    if pdf_content:
        text = re.sub(r"\n{3,}", "\n", pdf_content)
        text = re.sub('\s', ' ', text)
        text = text.replace("\n\n", "")
    sent_sep_pattern = re.compile(
        '([﹒﹔﹖﹗．。！？]["’”」』]{0,2}|(?=["‘“「『]{1,2}|$))')
    sent_list = []
    for ele in sent_sep_pattern.split(pdf_content):
        if sent_sep_pattern.match(ele) and sent_list:
            sent_list[-1] += ele
        elif ele:
            sent_list.append(ele)
    return sent_list


if __name__ == '__main__':
    # 读取pdf文档
    pdf_path = r'C:\Users\ASUS\Documents\WeChat Files\wxid_g3j0f2mugvwy22\FileStorage\File\2023-08\GBT 51353-2019 ' \
               r'住房公积金提取业务标准_.pdf'
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # 初始化结束页面为最后一页
        length = len(reader.pages)

        for page_num in range(0, length):
            page = reader.pages[page_num]
            text = page.extract_text()


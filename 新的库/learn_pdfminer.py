#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/1 11:05
# @Author   : FengYun
# @File     : learn_pdfminer.py
# @Software : PyCharm
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

# 打开PDF文件
with open(r'G:\文件\test\《12329住房公积金热线服务导则》.pdf', 'rb') as file:
    # 创建一个PDFResourceManager对象
    resource_manager = PDFResourceManager()

    # 创建一个StringIO对象，用于存储提取的文本内容
    output = StringIO()

    # 创建一个TextConverter对象
    converter = TextConverter(resource_manager, output, laparams=LAParams())

    # 创建一个PDFPageInterpreter对象
    interpreter = PDFPageInterpreter(resource_manager, converter)

    # 设置开始页码为2
    page_num = 1

    # 逐页解析文档
    for page in PDFPage.get_pages(file):
        if page_num >= 3:  # 从第二页开始转换
            interpreter = PDFPageInterpreter(resource_manager, converter)
            interpreter.process_page(page)

        page_num += 1

    # 获取提取的文本内容
    text = output.getvalue()
    print(text.strip().replace('\n', '').replace(' ', '').replace('-1-', '').replace('-2-', '').replace('-3-', '')
          .replace('-4-', '').replace('-5-', '').replace('-6-', '').replace('-7-', ''))

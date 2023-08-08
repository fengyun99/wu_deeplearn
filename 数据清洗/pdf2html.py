#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/2 13:44
# @Author   : FengYun
# @File     : pdf2html.py
# @Software : PyCharm
import fitz
from tqdm import tqdm


def pdf2html(input_path, html_path):
    doc = fitz.open(input_path)
    print(doc)
    html_content = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Title</title></head><body style=\"display: flex;justify-content: center;flex-direction: column;background: #0e0e0e;align-items: center;\">"
    for page in tqdm(doc):
        html_content += page.getText('html')
    print("开始输出html文件")

    html_content += "</body></html>"
    with open(html_path, 'w', encoding='utf8', newline="") as fp:
        fp.write(html_content)


input_path = r'G:\test\《会计档案管理办法》.pdf'  # 如果报错 就用绝对路径
html_path = r'G:\test\《会计档案管理办法》.pdf.html'
pdf2html(input_path, html_path)

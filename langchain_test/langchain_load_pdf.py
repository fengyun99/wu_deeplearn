#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/30 14:40
# @Author   : FengYun
# @File     : langchain_load_pdf.py
# @Software : PyCharm
from langchain.document_loaders import PyPDFLoader, UnstructuredPDFLoader

loader = PyPDFLoader(r"G:\test\满足规则二：《会计档案管理办法》.pdf")

pages = loader.load_and_split()

print(pages[0].page_content.lstrip('1'))
print('-------------------------------------------------------------------')

loader = UnstructuredPDFLoader(r"G:\test\满足规则二：《会计档案管理办法》.pdf")

data = loader.load()

print(data[0])
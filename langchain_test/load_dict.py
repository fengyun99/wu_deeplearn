#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/29 09:29
# @Author   : FengYun
# @File     : load_dict.py
# @Software : PyCharm
LOADER_DICT = {"UnstructuredFileLoader": ['.eml', '.html', '.json', '.md', '.msg', '.rst',
                                          '.rtf', '.txt', '.xml',
                                          '.doc', '.docx', '.epub', '.odt', '.pdf',
                                          '.ppt', '.pptx', '.tsv'],  # '.pdf', '.xlsx', '.csv'
               "CSVLoader": [".csv"],
               "PyPDFLoader": [".pdf"],
               }
SUPPORTED_EXTS = [ext for sublist in LOADER_DICT.values() for ext in sublist]
print(SUPPORTED_EXTS)

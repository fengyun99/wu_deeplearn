#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/5 17:28
# @Author   : FengYun
# @File     : text_split.py
# @Software : PyCharm
with open('data/员工手册.txt', 'r', encoding='utf-8') as f:
    state_of_the_union = f.read()

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(

    # 这里设置了一个很小的chunk_size，只是为了演示。

    chunk_size=1024,

    chunk_overlap=20,

    length_function=len,

)

texts = text_splitter.create_documents([state_of_the_union])

# print(texts[0].page_content)
#
# print(texts[1])

length = len(texts)
print(length)
with open('out.txt', 'w', encoding='utf-8') as f:
    for i in range(length):
        f.write(texts[i].page_content.replace('\n','') + '\n')





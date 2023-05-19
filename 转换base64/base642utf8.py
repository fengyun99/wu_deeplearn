#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/11 09:10
# @Author   : FengYun
# @File     : base642utf8.py
# @Software : PyCharm
import base64

# 文本
with open("data/base64.txt", "rb") as f:
    content = f.read()

# bytes内容进行分段处理
base64_contents = content.split(b'\n')
# 将所有的base64对象进行提取
base64_contents = [b64 for b64 in base64_contents if len(b64) > 0]

# 解码并转换为utf-8文本
for b64_content in base64_contents:
    # base64转为二进制文件
    binary_content = base64.b64decode(b64_content)
    # 再将二进制对象转为utf8
    utf8_content = binary_content.decode('utf-8')
    with open("../数据清洗/data/out.txt", "a", encoding="gbk", errors="replace") as f:
        # 错误编码\xa0无法解码，使用代替解决
        f.write(utf8_content.replace("\xa0",""))

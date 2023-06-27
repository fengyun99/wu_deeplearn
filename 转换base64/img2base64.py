#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/27 15:22
# @Author   : FengYun
# @File     : img2base64.py
# @Software : PyCharm
import base64


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string


# 用法示例
image_path = "data/test.jpg"
base64_string = image_to_base64(image_path)
print(base64_string)

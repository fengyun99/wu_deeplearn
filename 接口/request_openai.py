#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/25 16:23
# @Author   : FengYun
# @File     : request_openai.py
# @Software : PyCharm
import json
from enum import Enum
import requests


class RequestApi:
    def __init__(self, text):
        self.text = text

    # 单轮
    def input_text(self):
        url = "http://127.0.0.1:9999/apiQA/"
        data = {
            "input": self.text
        }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            content = response.json()
            return "回答:\n" + content['answer']
        else:
            return "对话失败"

if __name__ == '__main__':
    # 单轮
    text = input("对话:")
    res = RequestApi(text)
    print(res.input_text())

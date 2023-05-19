#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/24 17:29
# @Author   : FengYun
# @File     : request_api.py
# @Software : PyCharm
import json

import requests
'''
调用接口:只需要输入你的文本就可以转换为向量
'''
class RequestApi:
    def __init__(self, text):
        self.text = text

    def input_text(self):
        url = "http://192.168.2.103:8000/api/embeddings/"
        data = {
            "input": self.text
        }
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(url=url, data=json.dumps(data), headers=headers)
        content = response.json()
        return '向量: ' + str(content['data'][0]['embedding']) + '\nlength: ' + content['length']

if __name__ == '__main__':
    res = RequestApi("你好")
    print(res.input_text())
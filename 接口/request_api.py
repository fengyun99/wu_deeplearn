#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/24 17:29
# @Author   : FengYun
# @File     : request_api.py
# @Software : PyCharm
import requests
'''
调用接口:只需要输入你的文本就可以转换为向量
'''
class RequestApi:
    def __init__(self, text):
        self.text = text

    def input_text(self):
        url = "http://192.168.2.103:8000/input?input_str=" + self.text
        response = requests.get(url)
        print("向量是:" + response.json()[self.text])
        print("向量的长度" + response.json()['length'])

if __name__ == '__main__':
    res = RequestApi("公司注意项")
    res.input_text()
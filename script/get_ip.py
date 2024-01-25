#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/24 10:03
# @Author   : FengYun
# @File     : get_ip.py
# @Software : PyCharm
import requests


def get_public_ip():
    response = requests.get('http://ip-api.com/json')
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return data['query']
    return None


print(get_public_ip())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/24 10:04
# @Author   : FengYun
# @File     : get_ip_2.py
# @Software : PyCharm
import urllib.request


def get_ip():
    url = "https://api.ipify.org"
    response = urllib.request.urlopen(url)
    return response.read().decode()


print(get_ip())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/19 19:03
# @Author   : FengYun
# @File     : login.py
# @Software : PyCharm
import requests
url_tt = "https://accounts.pixiv.net/login"
url_login = "https://accounts.pixiv.net/ajax/login?lang=zh"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Content-Type": "application/json; charset=utf-",
    "Referer": "https://www.pixiv.net/"
}
session = requests.session()
tt = session.get(url_tt,headers=headers).content.decode("utf8")
# data = {
#     "login_id": "user_mxuc5288",
#     "password": "Awsl996!",
#     "source": "pc",
#     "return_to": "https://www.pixiv.net/",
#     "tt": tt.text
# }
#
#
# res = requests.post(url_login)
#
# print(res.status_code)
print(tt)
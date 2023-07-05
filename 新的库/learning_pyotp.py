#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/27 21:18
# @Author   : FengYun
# @File     : learning_pyotp.py
# @Software : PyCharm
# 生成/验证一次性密码(短信验证码)
import pyotp
import time

totp = pyotp.TOTP('base32secret3232')
print(totp.now())  # => '492039'

# OTP verified for current time
totp.verify('492039')  # => True
time.sleep(30)
totp.verify('492039')  # => False

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/11 14:33
# @Author   : FengYun
# @File     : MyError.py
# @Software : PyCharm
class NoMoneyError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    # 不会导致输出为__main__.NoMoneyError
    __module__ = 'builtins'

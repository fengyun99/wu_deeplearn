#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 16:22
# @Author   : FengYun
# @File     : 02.py
# @Software : PyCharm
# 定义水果类
class Fruit:
    def __init__(self, name):
        self.name = name


# 定义苹果类，继承自水果类
class Apple(Fruit):
    def __init__(self, name, variety):
        super().__init__(name)
        self.variety = variety


# 定义红苹果类，继承自苹果类
class RedApple(Apple):
    def __init__(self, name, variety, color):
        super().__init__(name, variety)
        self.color = color


# 定义红富士苹果类，继承自苹果类
class RedDeliciousApple(Apple):
    def __init__(self, name, variety, taste):
        super().__init__(name, variety)
        self.taste = taste


# 创建一个对象表示嘴里吃了一半的苹果
half_eaten_apple = RedApple("红苹果", "红富士", "红色")

print(f"我嘴里吃了一半的{half_eaten_apple.variety}苹果")

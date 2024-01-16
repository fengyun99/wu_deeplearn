#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 21:53
# @Author   : FengYun
# @File     : 01.py
# @Software : PyCharm
import pygame

# 初始函数，使用 pygame 的第一步；
pygame.init()
# 生成主屏幕 screen
screen = pygame.display.set_mode((600, 500), 0, 32)
# 设置标题
pygame.display.set_caption('Hello Pygame')
while True:
    # 刷新屏幕
    pygame.display.update()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 22:00
# @Author   : FengYun
# @File     : 02.py
# @Software : PyCharm
import pygame

pygame.init()
# 创建窗口
screen = pygame.display.set_mode((600, 500), 0, 32)
# 设置标题
pygame.display.set_caption('字体处理')
# 创建 font 对象
font = pygame.font.SysFont('kaiti', 20)
# 设置文本内容和颜色
COLOR_RED = pygame.Color(255, 255, 255)
textSurface = font.render('你好，Pygame', True, COLOR_RED)
# 设置文字的坐标
x, y = 5, 5
# 游戏主循环
while True:
    # 将文件添加到窗口
    screen.blit(textSurface, (x, y))
    pygame.display.update()

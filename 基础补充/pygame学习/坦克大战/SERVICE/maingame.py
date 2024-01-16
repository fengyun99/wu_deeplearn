#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 22:11
# @Author   : FengYun
# @File     : maingame.py
# @Software : PyCharm
import pygame

_display = pygame.display
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255, 255, 255)


class MainGame(object):
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800

    def __init__(self):
        pass

    # 开始游戏方法
    def startGame(self):
        _display.init()
        # 创建窗口加载窗口
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 设置一下游戏标题
        _display.set_caption("坦克大战 v1.03")

        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            MainGame.window.blit(self.getTextSurface('敌方剩余5'), (0, 0))
            # 窗口的刷新
            _display.update()

    # 左上角文字绘制的功能
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 选中一个合适的字体
        font = pygame.font.SysFont('kaiti', 18)
        # 使用对应的字符完成相关内容的绘制
        textSurface = font.render(text, True, COLOR_RED)
        return textSurface


MainGame().startGame()

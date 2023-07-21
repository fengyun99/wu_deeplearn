#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/20 17:25
# @Author   : FengYun
# @File     : 彩色.py
# @Software : PyCharm
from random import choice, randint, randrange
import string
from PIL import Image, ImageDraw, ImageFont


# 返回length长度随机字母和数字
def selectedCharacters(length):
    # string库
    result = ''.join(choice(string.ascii_letters + string.digits) for _ in range(length))
    return result


# 返回随机色
def getColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def makeIMG():
    # 图片属性
    size = [200, 100]
    characterNumber = 6
    bgcolor = (255, 255, 255)
    imageTemp = Image.new('RGB', size, bgcolor)
    draw = ImageDraw.Draw(imageTemp)
    text = selectedCharacters(characterNumber)
    font = ImageFont.truetype('c:\\windows\\fonts\\BRADHITC.TTF', 48)
    width, height = draw.textsize(text, font)

    # 判断尺寸
    if width + 2 * characterNumber > size[0] or height > size[1]:
        print('Dimension are not legitimate')
        return

    # 随机字符位置
    startX = 0
    widthEachCharater = width // characterNumber
    for i in range(characterNumber):
        startX += widthEachCharater + 1
        position = (startX, (size[1] - height) // 2 + randint(-5, 5))
        draw.text(xy=position, text=text[i], font=font, fill=getColor())

    # 对像素位置进行微调，实现扭曲的效果
    imageFinal = Image.new('RGB', size, bgcolor)
    pixelsFinal = imageFinal.load()
    pixelsTemp = imageTemp.load()
    for y in range(size[1]):
        offset = randint(-1, 0)
        for x in range(size[0]):
            newx = x + offset
            if newx >= size[0]:
                newx = size[0] - 1
            elif newx < 0:
                newx = 0
            pixelsFinal[newx, y] = pixelsTemp[x, y]

    # 随机色像素点
    draw = ImageDraw.Draw(imageFinal)
    for i in range(int(size[0] * size[1] * 0.05)):
        draw.point((randrange(size[0]), randrange(size[1])), fill=getColor())

    # 绘制5条随机干扰直线
    for i in range(3):
        start = (0, randrange(size[1]))
        end = (size[0], randrange(size[1]))
        draw.line([start, end], fill=getColor(), width=1)

    # 绘制5条随机弧线
    for i in range(3):
        start = (-50, -50)
        end = (size[0] + 10, randint(0, size[1] + 10))
        draw.arc(start + end, 0, 360, fill=getColor())

    imageFinal.save("image.jpg")


makeIMG()

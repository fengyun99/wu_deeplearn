#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/18 15:56
# @Author   : FengYun
# @File     : 练习6.py
# @Software : PyCharm
import random
import os
from PIL import Image, ImageFont, ImageDraw

'''
生成模糊的验证码图片
'''


def gen_code(Length):
    up_letter = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    down_letter = 'qwertyuiopasdfghjklzxcvbnm'
    number = '0123456789'
    Str = up_letter + down_letter + number
    Promo_Code = []
    for _ in range(Length):
        Promo_Code.append(random.choice(Str))
    return ''.join(Promo_Code)


# 随机颜色
def get_color():
    R = random.randrange(255)
    G = random.randrange(255)
    B = random.randrange(255)

    return (R, G, B)


def generate_image(code, width, height, font_size):
    # 创建一个新的图片对象
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    # 创建一个画笔对象
    draw = ImageDraw.Draw(img)
    # 设置字体
    font = ImageFont.truetype('arial.ttf', font_size)
    # 获取字符的宽度和高度
    # text_width, text_height = draw.textsize(code, font)
    # 获取字符的宽度和高度
    bbox = draw.textbbox((0, 0, width, height), code, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 将字符绘制在图片中央
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), code, font=font, fill=(0, 0, 0))
    # 添加干扰线
    for i in range(7):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=get_color(), width=2)
    # 添加干扰点
    for i in range(1000):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=get_color())
    # 返回验证码图片对象
    return img


def save_image(img, path):
    img.save(path)


if __name__ == '__main__':
    code = gen_code(4)
    img = generate_image(code, 150, 50, 30)
    save_image(img, "code.png")

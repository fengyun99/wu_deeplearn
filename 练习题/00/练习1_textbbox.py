#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/6 17:15
# @Author   : FengYun
# @File     : 练习1_textbbox.py
# @Software : PyCharm
from PIL import Image, ImageDraw, ImageFont

# 打开图像
image = Image.open("../img/self01.png")

# 创建一个副本，以便在上面添加水印
watermarked_image = image.copy()

# 设置水印文本
watermark_text = "5"

# 设置水印字体样式和大小
font = ImageFont.truetype("arial.ttf", 20)

# 创建一个绘图对象
draw = ImageDraw.Draw(watermarked_image)

# 获取水印文本的边界框
text_bbox = draw.textbbox((0, 0), watermark_text, font=font)

# 计算水印的位置（右上角）
padding = 10
position = (image.width - text_bbox[2] - padding, padding)

# 设置水印文本的颜色为红色
text_color = (255, 0, 0)  # 红色

# 添加水印文本到图像上
draw.text(position, watermark_text, font=font, fill=text_color)

# 保存带有水印的图像
watermarked_image.save("output_image.jpg")

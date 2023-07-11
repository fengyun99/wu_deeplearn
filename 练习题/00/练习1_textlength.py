#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/6 16:53
# @Author   : FengYun
# @File     : 练习1_textlength.py
# @Software : PyCharm
from PIL import Image, ImageDraw, ImageFont

# 打开图像
image = Image.open("../img/self01.png")

# 创建一个副本，以便在上面添加水印
watermarked_image = image.copy()

# 设置水印文本
watermark_text = "AAO"

# 设置水印字体样式和大小
font = ImageFont.truetype("arial.ttf", 20)

# 创建一个绘图对象
draw = ImageDraw.Draw(watermarked_image)

# 计算水印文本的长度,只能获得字段的长度
text_length = draw.textlength(watermark_text, font)

# 计算水印的位置（右上角）
padding = 0
position = (image.width - text_length - padding, image.height - text_length - padding)

# 设置水印文本的颜色为红色
text_color = (255, 0, 0)  # 红色

# 添加水印文本到图像上
draw.text(position, watermark_text, font=font, fill=text_color)

# 保存带有水印的图像
watermarked_image.save("output_image.jpg")

from PIL import Image, ImageDraw, ImageFont

# 打开图像
image = Image.open("../img/self01.png")

# 创建一个副本，以便在上面添加水印
watermarked_image = image.copy()

# 设置水印文本
watermark_text = "@赛马娘吧"

# 设置水印字体样式和大小,win+R,fonts下面属性名称就行。只有字体包含中文才能解析中文
font = ImageFont.truetype("msyh.ttc", 7)

# 创建一个绘图对象
draw = ImageDraw.Draw(watermarked_image)

# 获取文本的宽度和高度
text_width, text_height = draw.textsize(watermark_text, font)

# 计算水印的位置（右上角）
padding = 0
position = (image.width - text_width - padding, image.height - text_height - padding)

# 设置水印文本的颜色为红色
text_color = (255, 0, 0)  # 红色

# 添加水印文本到图像上
draw.text(position, watermark_text, font=font, fill=text_color)

# 保存带有水印的图像
watermarked_image.save("output_image.jpg")

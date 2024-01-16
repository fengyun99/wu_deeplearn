#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 21:08
# @Author   : FengYun
# @File     : 01.py
# @Software : PyCharm
# 导入模块
from tkinter import *
from tkinter import messagebox

# 创建窗口对象
root = Tk()
# 设置窗口的标题
root.title("tkinter 的第一个程序")
# 设置窗口的大小
# 宽度 500，高度 400；距屏幕左边 100，距屏幕上边 200
root.geometry("500x400+100+200")
# 创建组件
button = Button(root)
button['text'] = '点我有惊喜'
button.pack()


# 定义事件函数
def songhua(e):
    messagebox.showerror('Message', '送给你一朵玫瑰花')
    print('送给你一朵玫瑰花')


# 给控件绑定事件
button.bind('<Button-1>', songhua)
# 调用组件的 mainloop 方法，进入事件循环
root.mainloop()

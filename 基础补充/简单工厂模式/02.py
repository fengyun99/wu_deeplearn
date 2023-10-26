#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 15:15
# @Author   : FengYun
# @File     : 02.py
# @Software : PyCharm
# 定义伊兰特车类
class YilanteCar(object):
    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 定义索纳塔车类
class SuonataCar(object):
    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 定义一个生产汽车的工厂，让其根据具体的订单生产车
class CarFactory(object):
    def createCar(self, typeName):
        car = ''
        if typeName == "伊兰特":
            car = YilanteCar()
        elif typeName == "索纳塔":
            car = SuonataCar()
        return car


# 定义一个销售北京现代车的店类
class CarStore(object):
    def __init__(self):
        # 设置4s店的指定生产汽车的工厂
        self.carFactory = CarFactory()

    def order(self, typeName):
        # 让工厂根据类型，生产一辆汽车
        car = self.carFactory.createCar(typeName)
        return car

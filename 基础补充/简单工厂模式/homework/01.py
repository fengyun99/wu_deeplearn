#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/25 15:39
# @Author   : FengYun
# @File     : 01.py
# @Software : PyCharm
# 定义车类
class Car(object):
    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


class suonataCar(Car):
    # 定义车的方法
    def move(self):
        print("---索纳塔车在移动---")

    def stop(self):
        print("---索纳塔停车---")


class yilanteCar(Car):
    # 定义车的方法
    def move(self):
        print("---伊兰特车在移动---")

    def stop(self):
        print("---伊兰特停车---")


class carFactory(object):
    def createCar(self, type):
        if type == '索纳塔':
            car = suonataCar()
        elif type == '伊兰特':
            car = yilanteCar()
        return car


# 定义一个销售车的店类
class CarStore(object):
    def order(self, type):
        self.car = carFactory().createCar(type)  # 找一辆车
        self.car.move()
        self.car.stop()


c_s = CarStore()
c_s.order('索纳塔')

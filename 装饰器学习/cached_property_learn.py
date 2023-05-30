#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/29 13:30
# @Author   : FengYun
# @File     : cached_property_learn.py
# @Software : PyCharm
import random
import time

from cached_property import cached_property


# 实现缓存属性，同时设立方法能够删除缓存,当创建实例的时候就会一直存在
# @cached_property 等于 @property + @cache
class CacheTest:

    def insertionSort(self, arr):
        length = len(arr)
        for i in range(1, length):  # the current element index
            preIndex = i - 1  # the index to insert
            current = arr[i]  # save the number otherwise it will be replace by others
            while (preIndex >= 0 and arr[preIndex] > current):
                arr[preIndex + 1] = arr[preIndex]  # move -->
                preIndex -= 1
            arr[preIndex + 1] = current
        return arr

    @cached_property
    def test_operation(self):
        arr = [random.randint(0, 10000) for _ in range(1000)]
        result = self.insertionSort(arr)
        return result

    def cache_clear(self):
        del self.__dict__['test_operation']


if __name__ == '__main__':
    test_class = CacheTest()
    print(test_class.test_operation)
    # 直接返回结果不用计算
    print(test_class.test_operation)
    # 重新计算结果
    test_class.cache_clear()
    print(test_class.test_operation)
    # 创建不同的实例对象，重新返回
    test_class02 = CacheTest()
    print(test_class02.test_operation)

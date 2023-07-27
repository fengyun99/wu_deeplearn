#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/21 11:58
# @Author   : FengYun
# @File     : 多进程01.py
# @Software : PyCharm
'''
使用多进程实现在队列中按每5个取值，然后再给多进程处理
'''
import multiprocessing


def process_data(data, result_queue):
    # 将每个数字加1
    processed_data = [num + 1 for num in data]

    # 将结果放入队列中
    result_queue.put(processed_data)


if __name__ == "__main__":
    # 创建一个Manager对象
    manager = multiprocessing.Manager()

    # 创建一个共享的队列
    result_queue = manager.Queue()

    # 假设有一些数据，以列表形式存储
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # 创建多个进程，数量根据需要自行设定
    num_processes = 3
    processes = []

    for i in range(0, len(data_list), 5):
        start = i
        end = i + 5
        process = multiprocessing.Process(target=process_data, args=(data_list[start:end], result_queue))
        processes.append(process)

    # 启动进程
    for process in processes:
        process.start()

    # 等待所有进程执行完成
    for process in processes:
        process.join()

    # 从队列中获取处理后的结果并打印
    while not result_queue.empty():
        processed_data = result_queue.get()
        print("Processed data:", processed_data)

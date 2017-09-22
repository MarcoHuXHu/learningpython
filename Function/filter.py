#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter传入一个返回True或False的函数，与一个Iterable对象，返回经过函数筛选为True的元素
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# 结果: [1, 5, 9, 15]

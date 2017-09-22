#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map和reduce都是把函数作为参数传入，即高阶函数

from functools import reduce

# 0. 利用map和reduce来写一个str->int的函数
def str2int(str):
    def char2num(chr):
        dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return dic[chr]

    def nums2int(x, y):
        return x * 10 + y

    return reduce(nums2int, map(char2num, str))


print(str2int('123'))

# product, permutations

# 1. A x B
from itertools import product
import re
input_1a = '1, 2'
input_1b = '2, 3'
a = map(int, re.split(r'[\s,;]+', input_1a))
b = map(int, re.split(r'[\s,;]+', input_1b))

for i in product(a, b):
    print(i, end=" ")
print()

# 2. 排列
input2 = 'HACK 2'

from itertools import permutations
def join(a, b):
    return a + b

c, n = input().split(" ")
n = int(n)
for i in sorted(permutations(c, n)):
    print(reduce(join, i))

